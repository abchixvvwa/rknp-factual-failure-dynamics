# RKNP / LLM Factual Failure Dynamics
## Implementation Plan for Codex — Groq Free Tier Only

**Версия:** 1.0  
**Дата протокола:** 2026-09-10  
**Язык проекта и научной работы:** русский  
**Язык кода, имён переменных, README и таблиц данных:** английский  
**LLM-инференс:** только модели, доступные пользователю на бесплатном тарифе Groq  
**Запрещены:** платные LLM API, локальные генеративные LLM, OpenAI/Anthropic/Gemini API, платные embedding API.

---

# 0. Роль этого файла

Этот файл является главным execution plan для coding-agent/Codex.

Codex должен:

1. читать этот документ как основной source of truth;
2. реализовывать проект по фазам;
3. не перепрыгивать через обязательные проверки;
4. не выдумывать результаты;
5. не подменять научный эксперимент красивым приложением;
6. сохранять сырые данные и конфигурацию каждого запуска;
7. не использовать test set для выбора модели, признаков, threshold или гиперпараметров;
8. соблюдать ограничения Groq Free Tier;
9. работать resume-safe: любой длинный эксперимент должен продолжаться после остановки, а не начинаться заново;
10. после каждой фазы обновлять `STATUS.md`.

Если этот файл конфликтует с импровизированным решением агента — следовать этому файлу, пока пользователь явно не изменит протокол.

---

# 1. Название проекта

## Русское рабочее название

**Разработка метода прогнозирования фактических ошибок больших языковых моделей на основе динамики семантической согласованности и неопределённости генерации**

## Английское рабочее название

**Predicting Factual Failures in Large Language Models through Semantic Consistency Dynamics and Generation Uncertainty**

---

# 2. Главная идея

Мы не строим обычный "hallucination detector".

Мы исследуем, можно ли оценить вероятность того, что основной ответ LLM фактически неверен, анализируя **поведение той же модели при нескольких независимых генерациях**.

Для одного вопроса:

```text
Question
   │
   ├── Target answer: low-temperature response
   │
   ├── Sample 1
   ├── Sample 2
   ├── Sample 3
   ├── Sample 4
   └── Sample 5
            │
            ▼
   semantic grouping
            │
            ▼
   uncertainty trajectory
   k = 2 → 3 → 4 → 5
            │
            ▼
    factual-risk model
            │
            ▼
      P(error) ∈ [0, 1]
```

Ключевой объект исследования — не только финальный disagreement, а **динамика формирования согласия/несогласия** по мере добавления новых генераций.

---

# 3. Критическая особенность Groq API

Проект должен быть спроектирован под реальные ограничения Groq.

## 3.1 Только Groq

Все генеративные LLM-вызовы выполняются через:

```text
https://api.groq.com/openai/v1
```

или официальный `groq` Python SDK.

API key:

```text
GROQ_API_KEY
```

Никогда не коммитить API key.

---

## 3.2 Logprobs не использовать

На момент фиксации этого протокола Groq Chat API не предоставляет поддерживаемые `logprobs/top_logprobs` для доступных моделей.

Поэтому:

**НЕ реализовывать token-logprob entropy как основной признак.**

Термин "generation uncertainty" в проекте операционализируется как **эмпирическая неопределённость распределения ответов**, измеренная через повторные стохастические генерации:

- semantic entropy;
- cluster entropy;
- disagreement;
- dominant-answer share;
- cluster growth;
- consensus stability;
- response switching;
- trajectory dynamics.

Если Groq когда-либо добавит logprobs, не включать их в основной эксперимент без новой версии протокола.

---

## 3.3 `n=1`

Groq Chat API поддерживает `n=1`.

Поэтому 5 sampled answers = 5 отдельных API requests.

Нужно реализовать:

- очередь;
- rate limiting;
- retry;
- exponential backoff;
- resume;
- deduplication;
- persistent progress.

---

## 3.4 Temperature

Для target answer использовать:

```yaml
temperature: 0.0
seed: 42
```

Groq может внутренне преобразовывать `temperature=0` в очень малое положительное значение.

Это допустимо.

Target generation считается **low-temperature reference generation**, а не математически гарантированно deterministic generation.

Сохранять `system_fingerprint` из ответа API.

---

# 4. Модели Groq

Нельзя полагаться на то, что список моделей останется неизменным.

Перед pilot и перед main experiment выполнить:

```text
GET /openai/v1/models
```

и сохранить snapshot:

```text
artifacts/groq/model_snapshot_YYYYMMDD.json
```

## 4.1 Preferred target models

Если доступны на Free Tier:

```yaml
target_models:
  - openai/gpt-oss-20b
  - qwen/qwen3.6-27b
  - qwen/qwen3.8-27b
```

## 4.2 Semantic judge

Preferred:

```yaml
semantic_judge_model: openai/gpt-oss-120b
```

Judge используется **только** для:

- semantic equivalence;
- semantic clustering;
- структурирования неоднозначных ответов.

Judge **НЕ является источником ground truth factual correctness**.

## 4.3 Если модель недоступна

Не заменять молча.

Сделать:

1. получить текущий `/models`;
2. записать недоступную модель в лог;
3. выбрать замену только из моделей, реально доступных пользователю на Groq Free Tier;
4. записать замену в `STATUS.md`;
5. сохранить новый config;
6. не менять уже начатый основной эксперимент посередине без отдельного experiment ID.

---

# 5. Groq Free Tier budget

Код должен считать API budget.

Создать:

```text
src/groq/budget.py
```

Он ведёт:

- requests today;
- requests per model;
- estimated input tokens;
- actual input tokens from API usage;
- output tokens;
- 429 count;
- retry count.

Длинные запуски должны уметь завершаться корректно при достижении дневного лимита и продолжаться на следующий запуск.

Никаких попыток обходить rate limits несколькими аккаунтами/организациями.

---

# 6. Research questions

## RQ1

**Можно ли предсказывать фактическую ошибку основного ответа LLM по семантической вариативности её независимых генераций?**

## RQ2

**Даёт ли динамика изменения согласованности при k=2,3,4,5 дополнительный predictive signal относительно статического измерения на k=5?**

## RQ3

**Насколько этот сигнал переносится между English, Russian и Kazakh?**

## RQ4

**Насколько этот сигнал переносится между разными моделями Groq?**

## RQ5

**Можно ли адаптивно остановить sampling раньше 5 генераций и сохранить близкое качество обнаружения ошибок?**

---

# 7. Гипотезы

## H1 — disagreement

Фактически неверные target answers имеют в среднем более высокую вариативность sampled answers.

## H2 — semantic entropy

Semantic entropy sampled answers выше для фактически неверных target answers.

## H3 — dynamics

Dynamic trajectory features улучшают AUROC относительно static consistency features.

## H4 — multilingual effect

Predictive quality отличается между EN/RU/KZ.

Не утверждать заранее, какой язык окажется хуже.

## H5 — cross-model generalization

Часть признаков uncertainty переносится на модель, которую risk classifier не видел при обучении.

## H6 — adaptive sampling

Adaptive stopping снижает среднее число API generations при ограниченном снижении recall ошибок.

---

# 8. Что считается научной новизной

Не заявлять, что проект "изобрёл semantic entropy" или "первым обнаруживает hallucinations".

Рабочая предполагаемая новизна:

1. **trajectory-based analysis** — анализ изменения semantic uncertainty по мере появления новых samples;
2. **multilingual controlled benchmark** — один и тот же факт проверяется на EN/RU/KZ;
3. **cross-model transfer** — проверка переносимости risk features между несколькими Groq-hosted LLM;
4. **adaptive sampling** — ранняя остановка при достаточной уверенности;
5. **resource-constrained setting** — метод работает без logits, без внешнего retrieval и без платного inference.

После literature review формулировку novelty необходимо проверить и при необходимости сузить.

---

# 9. Что запрещено делать

Не делать:

- RAG как главный метод;
- web search для проверки каждого target response;
- "AI fact checker" как основной продукт;
- frontend до завершения экспериментов;
- LLM-as-a-judge как единственный factual labeler;
- фиктивный датасет без источников;
- автоматически созданные "источники";
- выдуманные confidence values;
- synthetic test results;
- вручную менять test labels ради улучшения score;
- выбирать признаки после просмотра test performance;
- использовать test set для threshold tuning;
- скрывать failed API calls;
- удалять неудобные outliers без документированной причины.

---

# 10. Репозиторий

Создать следующую структуру:

```text
rknp-factual-dynamics/
│
├── README.md
├── IMPLEMENTATION_PLAN.md
├── RESEARCH_PROTOCOL.md
├── STATUS.md
├── CHANGELOG.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── configs/
│   ├── groq.yaml
│   ├── models.yaml
│   ├── generation.yaml
│   ├── experiment.yaml
│   └── paths.yaml
│
├── data/
│   ├── benchmark/
│   │   ├── facts.csv
│   │   └── README.md
│   ├── labels/
│   │   ├── manual_review_queue.csv
│   │   └── reviewed_labels.csv
│   └── processed/
│       └── splits.csv
│
├── artifacts/
│   ├── groq/
│   ├── generations/
│   ├── semantic_judgments/
│   ├── features/
│   └── models/
│
├── experiments/
│   ├── pilot/
│   ├── main/
│   ├── cross_language/
│   ├── cross_model/
│   ├── ablation/
│   └── adaptive/
│
├── results/
│   ├── metrics/
│   ├── tables/
│   ├── figures/
│   └── reports/
│
├── src/
│   ├── benchmark/
│   │   ├── schema.py
│   │   ├── validate.py
│   │   └── split.py
│   │
│   ├── groq/
│   │   ├── client.py
│   │   ├── models.py
│   │   ├── limiter.py
│   │   ├── retry.py
│   │   └── budget.py
│   │
│   ├── generation/
│   │   ├── prompts.py
│   │   ├── scheduler.py
│   │   ├── store.py
│   │   └── run.py
│   │
│   ├── labeling/
│   │   ├── normalize.py
│   │   ├── exact_match.py
│   │   ├── numeric_match.py
│   │   ├── date_match.py
│   │   ├── manual_queue.py
│   │   └── build_labels.py
│   │
│   ├── semantics/
│   │   ├── lexical.py
│   │   ├── judge.py
│   │   ├── clustering.py
│   │   └── validate_judge.py
│   │
│   ├── uncertainty/
│   │   ├── entropy.py
│   │   ├── static_features.py
│   │   └── trajectories.py
│   │
│   ├── features/
│   │   ├── schema.py
│   │   └── build.py
│   │
│   ├── modeling/
│   │   ├── baselines.py
│   │   ├── train.py
│   │   ├── calibration.py
│   │   └── save.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   ├── bootstrap.py
│   │   ├── subgroup.py
│   │   ├── cross_language.py
│   │   ├── cross_model.py
│   │   └── ablation.py
│   │
│   ├── adaptive/
│   │   ├── policy.py
│   │   └── simulate.py
│   │
│   └── utils/
│       ├── io.py
│       ├── hashing.py
│       ├── logging.py
│       ├── seeds.py
│       └── time.py
│
├── scripts/
│   ├── 00_check_environment.py
│   ├── 01_snapshot_groq_models.py
│   ├── 02_validate_benchmark.py
│   ├── 03_make_splits.py
│   ├── 04_run_pilot_generation.py
│   ├── 05_build_target_labels.py
│   ├── 06_run_semantic_clustering.py
│   ├── 07_build_features.py
│   ├── 08_train_baselines.py
│   ├── 09_train_dynamic_model.py
│   ├── 10_evaluate_validation.py
│   ├── 11_run_main_generation.py
│   ├── 12_freeze_pipeline.py
│   ├── 13_evaluate_test.py
│   ├── 14_cross_language.py
│   ├── 15_cross_model.py
│   ├── 16_ablation.py
│   ├── 17_adaptive_sampling.py
│   └── 18_build_report.py
│
├── tests/
│   ├── test_benchmark.py
│   ├── test_splits.py
│   ├── test_normalization.py
│   ├── test_entropy.py
│   ├── test_trajectory.py
│   ├── test_resume.py
│   └── test_metrics.py
│
└── demo/
    └── app.py
```

---

# 11. Python dependencies

Минимум:

```text
groq
pandas
numpy
scipy
scikit-learn
pyarrow
pydantic
pyyaml
tenacity
tqdm
rapidfuzz
matplotlib
joblib
pytest
```

Demo later:

```text
streamlit
```

Не добавлять тяжёлые локальные LLM/embedding dependencies без необходимости.

---

# 12. Environment

`.env.example`:

```env
GROQ_API_KEY=
```

`.gitignore` обязан включать:

```text
.env
*.key
artifacts/generations/*
artifacts/groq/private/*
```

Raw research artifacts можно хранить вне Git или через отдельное release/archive storage.

---

# 13. Benchmark design

## 13.1 Основная единица

`fact_id` = один проверяемый факт/вопрос.

Один `fact_id` имеет три языковых версии:

- EN
- RU
- KZ

Смысл вопроса должен быть максимально эквивалентным.

---

## 13.2 Pilot size

```text
100 unique facts
× 3 languages
= 300 language-prompts
```

---

## 13.3 Main size

Целевая версия:

```text
500 unique facts
× 3 languages
= 1500 language-prompts
```

Если Free Tier budget делает это слишком медленным, разрешено выполнить main на 300 facts, но это решение должно быть принято **до test evaluation** и записано в `RESEARCH_PROTOCOL.md`.

---

# 14. Benchmark categories

Целевая структура для 500 facts:

| Category | Facts |
|---|---:|
| history | 80 |
| geography | 80 |
| science | 80 |
| culture | 80 |
| kazakhstan | 80 |
| adversarial_false_premise | 100 |
| **TOTAL** | **500** |

Для pilot использовать пропорциональный subset.

---

# 15. Benchmark CSV schema

Файл:

```text
data/benchmark/facts.csv
```

Поля:

```text
fact_id
category
difficulty
question_type
question_en
question_ru
question_kk
canonical_answer
acceptable_aliases_json
false_premise
source_url
source_title
source_publisher
source_accessed_date
notes
verified_by_human
```

Constraints:

- `fact_id` unique;
- все три question-поля заполнены;
- `canonical_answer` заполнен;
- `source_url` обязателен;
- `verified_by_human=true` обязателен для попадания в main experiment.

---

# 16. Question types

Минимум:

```text
entity
numeric
date
direct_fact
false_premise
```

Не использовать длинные open-ended questions как основной benchmark.

Нам нужны вопросы, factual correctness которых можно reasonably определить.

---

# 17. False-premise subset

Пример логики:

```text
Question contains a false assumption.
Correct behavior:
- explicitly reject premise
- or state that the described event/entity does not exist
```

Для таких записей:

```text
false_premise = true
```

В `acceptable_aliases_json` хранить допустимые формулировки отказа/исправления только если они достаточно формализуемы.

Не делать все adversarial questions автоматически созданными одной LLM без ручной проверки.

---

# 18. Ground truth

Ground truth не создаётся target LLM и не создаётся semantic judge.

Каждый факт должен иметь:

- canonical answer;
- authoritative source;
- human verification.

Если факт спорный или зависит от интерпретации — исключить до freeze benchmark.

---

# 19. Split protocol

Split выполняется **по `fact_id`**, а не по отдельным language rows.

Пропорции:

```text
train = 70%
validation = 15%
test = 15%
```

Seed:

```text
42
```

Сохранить:

```text
data/processed/splits.csv
```

Поля:

```text
fact_id
split
```

Обязательные assertions:

```text
no fact_id appears in multiple splits
all benchmark fact_ids are assigned
category distribution is approximately stratified
```

---

# 20. Freeze benchmark

После создания основного benchmark:

1. отсортировать по `fact_id`;
2. сохранить CSV;
3. вычислить SHA-256;
4. записать hash в `RESEARCH_PROTOCOL.md`;
5. после начала main experiment содержимое benchmark не менять.

Если обнаружена ошибка:

- создать `facts_v2.csv`;
- новый hash;
- документировать причину;
- не смешивать результаты v1 и v2.

---

# 21. Generation prompt

Все target models должны получать эквивалентный prompt.

Ответ должен быть коротким, чтобы:

- снизить Groq token usage;
- уменьшить лишнюю вариативность;
- облегчить factual labeling.

## EN

```text
Answer the factual question briefly and directly.
If the question contains a false premise, explicitly say that the premise is false.
If you do not know the answer, say that you do not know.
Do not invent facts.

Question:
{question}
```

## RU

```text
Кратко и прямо ответь на фактический вопрос.
Если вопрос содержит ложную предпосылку, явно укажи, что предпосылка неверна.
Если ты не знаешь ответа, скажи, что не знаешь.
Не выдумывай факты.

Вопрос:
{question}
```

## KZ

Создать качественный эквивалентный казахский prompt и **обязательно вручную проверить его до main experiment**.

Prompt version:

```text
factual_v1
```

---

# 22. Generation protocol

Для каждой комбинации:

```text
fact_id × language × target_model
```

получить:

## 22.1 Target answer

```yaml
generation_type: target
temperature: 0.0
seed: 42
max_completion_tokens: 96
```

## 22.2 Sampled answers

Количество:

```text
5
```

Параметры:

```yaml
generation_type: sample
temperature: 0.7
top_p: 0.95
max_completion_tokens: 96
seeds:
  - 101
  - 202
  - 303
  - 404
  - 505
```

Не использовать `n=5`; выполнять отдельные requests.

---

# 23. Request count

При 500 facts:

```text
500 facts
× 3 languages
× 3 target models
× (1 target + 5 samples)
= 27,000 target-model requests
```

Semantic clustering requests считаются отдельно.

Поэтому pipeline обязан быть multi-day и resume-safe.

Pilot:

```text
100 × 3 × 3 × 6
= 5,400 target-model requests
```

Если pilot слишком дорог по free daily budget, начать с 50 facts и 2 target models как engineering smoke test, но scientific pilot должен быть зафиксирован отдельно.

---

# 24. Raw generation storage

Основной файл:

```text
artifacts/generations/generations.parquet
```

Одна строка = один API response.

Поля:

```text
run_id
request_id
fact_id
language
model_id
generation_type
sample_index
prompt_version
prompt_text
response_text
temperature
top_p
seed
max_completion_tokens
created_at_utc
latency_ms
prompt_tokens
completion_tokens
total_tokens
system_fingerprint
finish_reason
http_status
retry_count
error_type
error_message
response_sha256
```

Unique key:

```text
fact_id + language + model_id + generation_type + sample_index + prompt_version + experiment_id
```

Перед API call проверять, существует ли успешная запись с этим key.

Если да — skip.

---

# 25. Rate limiter

`src/groq/limiter.py` должен:

- ограничивать RPM;
- отслеживать TPM;
- читать rate-limit response headers, когда доступны;
- уважать `retry-after`;
- делать jittered exponential backoff;
- не спамить API после 429;
- корректно переживать сетевые ошибки.

Retry policy:

```text
429 → respect retry-after
5xx → exponential backoff
timeout → retry
400 → do not retry blindly
401/403 → stop run and report
```

Максимум повторов configurable.

---

# 26. Resume mechanism

После каждого успешного response:

1. немедленно persist;
2. flush/checkpoint;
3. обновить progress summary.

При crash:

```bash
python scripts/04_run_pilot_generation.py
```

должен продолжить с отсутствующих keys.

Никакого полного перезапуска.

---

# 27. Target factual labeling

Для каждого target answer создать:

```text
is_factually_correct ∈ {0, 1}
```

и:

```text
label_status
```

Допустимые statuses:

```text
auto_correct
auto_incorrect
manual_correct
manual_incorrect
unresolved
```

---

# 28. Automatic labeling

Разрешены:

- case normalization;
- Unicode normalization;
- whitespace normalization;
- punctuation normalization;
- exact canonical match;
- acceptable alias match;
- numeric equivalence;
- date equivalence;
- transparent regex rules.

Все правила тестировать unit tests.

---

# 29. Manual review

Если автоматический matcher не уверен:

экспортировать в:

```text
data/labels/manual_review_queue.csv
```

Поля:

```text
fact_id
language
model_id
question
canonical_answer
acceptable_aliases
target_response
auto_reason
review_label
review_notes
reviewer
```

Main evaluation использует только resolved labels.

Количество unresolved cases обязательно отчётить.

---

# 30. Semantic consistency: принцип

Поскольку внешние embedding models не используются, semantic grouping выполняется гибридно:

## Stage A — deterministic equivalence

Сначала проверить:

- exact normalized answer;
- numeric equivalence;
- date equivalence;
- high lexical equivalence через `rapidfuzz`.

## Stage B — Groq semantic judge

Если equivalence не определяется rules:

отправить **все 5 samples одного case одним запросом** fixed semantic judge model.

Judge получает только:

- question;
- five responses.

Он **не получает canonical ground truth**.

Его задача:

> сгруппировать ответы, выражающие один и тот же фактический ответ/утверждение.

---

# 31. Semantic judge prompt

Использовать JSON output.

Пример:

```text
You are evaluating semantic agreement between candidate answers.

Do NOT decide which answer is factually correct.
Do NOT use external knowledge.
Only group answers that make the same factual claim.

Question:
{question}

Answers:
A: ...
B: ...
C: ...
D: ...
E: ...

Return JSON:
{
  "groups": [
    {"group_id": 0, "members": ["A", "C", "E"]},
    {"group_id": 1, "members": ["B"]},
    {"group_id": 2, "members": ["D"]}
  ],
  "uncertain": false
}
```

Judge temperature:

```text
0.0
```

Fixed seed.

---

# 32. Judge cache

Сохранять:

```text
artifacts/semantic_judgments/judgments.parquet
```

Поля:

```text
case_id
judge_model
judge_prompt_version
question
sample_hashes
raw_judge_response
parsed_groups_json
judge_uncertain
created_at
system_fingerprint
```

Если sample hashes совпадают — повторно judge не вызывать.

---

# 33. Judge validation

Semantic judge сам может ошибаться.

Поэтому обязательно сделать validation subset.

Минимум:

```text
200 cases
```

случайно выбранных и стратифицированных по языку/model/category.

Человек вручную группирует samples по смыслу.

Сравнить judge vs human:

- Adjusted Rand Index;
- pairwise agreement;
- процент exact cluster match.

Если agreement неудовлетворительный, метод semantic clustering пересмотреть **до main test evaluation**.

---

# 34. Lexical baselines

Даже если semantic judge используется, обязательно считать model-free lexical features:

```text
mean_pairwise_token_jaccard
mean_pairwise_rapidfuzz_ratio
min_pairwise_rapidfuzz_ratio
lexical_diversity
normalized_answer_unique_count
```

Это даст baseline:

> действительно ли semantic grouping лучше простой строковой похожести?

---

# 35. Semantic clusters

Для каждого case после grouping получить labels:

```text
sample_1 -> cluster 0
sample_2 -> cluster 1
sample_3 -> cluster 0
sample_4 -> cluster 0
sample_5 -> cluster 2
```

Cluster sizes:

```text
[3, 1, 1]
```

---

# 36. Static uncertainty features

Вычислить:

```text
n_clusters
largest_cluster_fraction
second_largest_cluster_fraction
consensus_margin
disagreement_rate
semantic_entropy
normalized_semantic_entropy
unique_normalized_answers
```

## Semantic entropy

```text
H = -Σ p_i * ln(p_i)
```

где:

```text
p_i = cluster_size_i / number_of_samples
```

Normalized:

```text
H_norm = H / ln(K_max)
```

Обработать случай одного cluster:

```text
H = 0
```

---

# 37. Target-to-consensus features

Сопоставить target answer с semantic groups samples.

Получить:

```text
target_matches_dominant_cluster
target_cluster_fraction
target_supported_by_n_samples
target_support_ratio
```

Важно:

это **не factual label**.

Это только self-consistency signal.

Модель может быть consistently wrong.

---

# 38. Dynamic trajectories

Для prefix samples:

```text
k = 2
k = 3
k = 4
k = 5
```

пересчитать:

```text
H_k
n_clusters_k
largest_cluster_fraction_k
target_support_ratio_k
disagreement_rate_k
```

Не использовать будущие samples при расчёте prefix k.

---

# 39. Dynamic features

Из trajectory извлечь:

```text
entropy_k2
entropy_k3
entropy_k4
entropy_k5

entropy_slope
entropy_auc
entropy_last_delta
entropy_max_delta
entropy_variance

cluster_count_k2
cluster_count_k3
cluster_count_k4
cluster_count_k5
cluster_births

dominant_fraction_slope
dominant_fraction_min
dominant_fraction_final

target_support_slope
target_support_min
target_support_final

consensus_switch_count
stabilization_step
late_disagreement_flag
```

Все формулы написать в:

```text
RESEARCH_PROTOCOL.md
```

---

# 40. Stabilization definition

Working definition:

Consensus считается stabilized на step `k`, если:

1. dominant semantic cluster после step `k` больше не меняется;
2. изменение normalized entropy для последующих steps меньше threshold `epsilon`.

`epsilon` выбирается **только по validation set**.

Не подбирать по test.

---

# 41. Feature table

Создать:

```text
artifacts/features/features.parquet
```

Одна строка:

```text
fact_id × language × target_model
```

Поля:

```text
case_id
fact_id
split
language
category
difficulty
question_type
target_model
is_factually_correct
error_label
...
static features
dynamic features
lexical features
```

Для risk prediction target:

```text
error_label = 1 - is_factually_correct
```

---

# 42. Baselines

Обязательные baselines:

## B0 — Prior/Dummy

```text
DummyClassifier(strategy="prior")
```

## B1 — Unique answer count

Risk score based on number of unique normalized answers.

## B2 — Lexical disagreement

Risk from RapidFuzz/Jaccard features.

## B3 — Final semantic entropy

Один static feature.

## B4 — Final semantic consistency model

Logistic Regression только на static semantic features.

## B5 — Target support

Risk based on target support ratio.

---

# 43. Proposed method

Главная модель:

**Dynamic Semantic Uncertainty Model**

Input:

```text
static semantic features
+
target-support features
+
dynamic trajectory features
```

Начать с:

```text
LogisticRegression
```

Затем сравнить на validation:

```text
RandomForestClassifier
HistGradientBoostingClassifier
```

Не использовать deep neural network просто ради сложности.

---

# 44. Training protocol

Train:

```text
train split
```

Model selection:

```text
validation split
```

Final evaluation:

```text
test split
```

Preprocessing pipeline должен быть внутри sklearn Pipeline, чтобы избежать leakage.

Если есть missing values — imputation fit только на train.

Scaling fit только на train.

---

# 45. Primary metric

Главная метрика:

```text
AUROC
```

Secondary:

```text
AUPRC
F1
Precision
Recall
Accuracy
Brier Score
ECE
```

Если error class сильно imbalanced, AUPRC должна обсуждаться отдельно.

---

# 46. Threshold selection

Threshold для classification выбирать на validation.

Возможные критерии:

```text
max F1
```

или, для практического режима:

```text
Recall(error) >= 0.90
with maximal precision
```

Выбранный критерий зафиксировать до test evaluation.

---

# 47. Calibration

Оценить probability calibration.

Сравнить:

- raw;
- sigmoid/Platt;
- isotonic.

Выбор только на validation.

Сохранить:

```text
calibration curve
Brier score
ECE
```

---

# 48. Bootstrap confidence intervals

Для test metrics:

```text
1000 bootstrap resamples
95% CI
```

Resampling unit:

```text
fact_id
```

а не отдельная language/model row.

Причина: EN/RU/KZ versions одного fact зависимы.

---

# 49. Statistical comparison

Для ключевого сравнения:

```text
Static model vs Dynamic model
```

оценить bootstrap distribution:

```text
ΔAUROC
ΔAUPRC
```

Сохранить 95% CI.

Не утверждать "significant improvement", если CI не поддерживает утверждение.

---

# 50. Cross-language experiment

Эксперименты:

```text
Train EN → Test RU
Train EN → Test KZ
Train RU → Test EN
Train RU → Test KZ
Train EN+RU → Test KZ
```

Использовать фиксированный feature pipeline.

Отчёт:

```text
in-language score
cross-language score
absolute drop
relative drop
```

---

# 51. Cross-model experiment

Leave-one-model-out:

```text
Train target_model_A + target_model_B
Test target_model_C
```

Повторить для всех target models.

Важно:

если модели принадлежат только двум model families, не писать "полная cross-family generalization".

Писать аккуратно:

> cross-model generalization across the evaluated Groq-hosted models.

---

# 52. Language × model matrix

Обязательная итоговая таблица:

| Model | EN AUROC | RU AUROC | KZ AUROC |
|---|---:|---:|---:|
| Model A | real | real | real |
| Model B | real | real | real |
| Model C | real | real | real |

Никаких placeholder numbers в финальном report.

---

# 53. Category analysis

Отдельно:

```text
history
geography
science
culture
kazakhstan
false premise
```

Оценить:

- factual error rate;
- semantic entropy distribution;
- detector AUROC, если sample size достаточен.

Не делать сильные выводы по tiny subgroups.

---

# 54. Ablation study

Главный ablation:

```text
FULL
STATIC_ONLY
DYNAMIC_ONLY
NO_TARGET_SUPPORT
NO_CLUSTER_ENTROPY
LEXICAL_ONLY
```

Сравнить:

```text
AUROC
AUPRC
Brier
```

Цель:

показать, что именно даёт proposed dynamic method.

---

# 55. Adaptive sampling

После обучения risk model симулировать sequential sampling.

После k samples:

```text
k = 2
k = 3
k = 4
```

оценить current risk.

Решение:

```text
if risk <= low_threshold:
    stop -> low risk

elif risk >= high_threshold:
    stop -> high risk

else:
    request next sample
```

Maximum:

```text
5 samples
```

---

# 56. Adaptive policy selection

`low_threshold` и `high_threshold` выбирать только на validation.

Цель:

минимизировать:

```text
average_samples_per_case
```

при constraint, например:

```text
error recall degradation <= chosen tolerance
```

Tolerance зафиксировать до test adaptive evaluation.

---

# 57. Adaptive metrics

Отчёт:

```text
average_samples
median_samples
p90_samples
percentage_stopped_at_2
percentage_stopped_at_3
percentage_stopped_at_4
percentage_reaching_5

AUROC
Recall(error)
API request reduction
```

API request reduction:

```text
1 - adaptive_sample_requests / fixed_5_sample_requests
```

---

# 58. Pilot experiment

## Цель pilot

Не доказать гипотезу.

Цель:

- проверить pipeline;
- измерить factual error prevalence;
- проверить sample diversity;
- проверить judge reliability;
- определить feasibility;
- проверить Groq limits;
- оценить время main experiment.

---

# 59. Pilot phases

## Pilot A — engineering smoke test

```text
10 facts
3 languages
2 target models
```

Проверить end-to-end.

Не использовать эти результаты как scientific result.

## Pilot B — scientific pilot

Цель:

```text
100 facts
3 languages
3 models
5 samples
```

Если API budget мешает, разрешается:

```text
100 facts
3 languages
2 models
```

но это изменение фиксируется до запуска.

---

# 60. Pilot exit criteria

Не начинать main, пока не выполнено:

- [ ] no duplicate generation keys
- [ ] resume works
- [ ] 429 correctly handled
- [ ] benchmark validation passes
- [ ] split leakage test passes
- [ ] factual labeling pipeline works
- [ ] semantic judge JSON parse success >= 99%
- [ ] manual judge-validation sample completed
- [ ] feature table builds without silent errors
- [ ] baselines train
- [ ] trajectories verified manually on examples
- [ ] estimated main runtime documented
- [ ] estimated daily request budget documented

---

# 61. Main experiment freeze

Перед main:

создать:

```text
experiments/main/FROZEN_CONFIG.yaml
```

В нём:

```text
benchmark_sha256
split_sha256
prompt_version
target_models
judge_model
generation_parameters
sample_count
feature_version
semantic_judge_prompt_version
classifier_candidates
primary_metric
random_seed
```

После freeze не менять config на основе test results.

---

# 62. Test evaluation lock

Скрипт:

```text
scripts/13_evaluate_test.py
```

должен проверять наличие:

```text
experiments/main/FROZEN_CONFIG.yaml
```

и trained artifact выбранного model.

Рекомендуется создать marker:

```text
experiments/main/TEST_EVALUATED.lock
```

Если marker существует, повторный test evaluation требует явного флага:

```text
--allow-repeat
```

и записывается в audit log.

---

# 63. Reproducibility

Для каждого experiment сохранить:

```text
experiment_id
git_commit
python_version
package_versions
config_hash
benchmark_hash
split_hash
model_snapshot_hash
timestamp
```

Скрипт:

```text
src/utils/reproducibility.py
```

---

# 64. Logging

Структурированные логи:

```text
logs/{experiment_id}.jsonl
```

Каждый event:

```json
{
  "timestamp": "...",
  "level": "INFO",
  "event": "groq_request_success",
  "case_id": "...",
  "model_id": "...",
  "details": {}
}
```

Не логировать API key.

---

# 65. Tests

Минимум:

## Benchmark

- duplicate fact_id fails;
- missing source fails;
- missing language fails;
- unverified main row fails.

## Split

- no leakage;
- deterministic with same seed.

## Generation store

- duplicate key ignored;
- retry does not create duplicate successful row;
- resume finds missing work.

## Normalization

- casing;
- Unicode;
- numeric formats;
- dates.

## Entropy

Known distributions:

```text
[1.0] -> H=0
[0.5,0.5] -> expected value
```

## Dynamics

Hand-created cluster sequences with expected trajectory.

## Metrics

Compare with known sklearn output.

---

# 66. CLI behavior

Каждый script должен поддерживать:

```text
--config
--experiment-id
--dry-run
--limit
```

Generation scripts дополнительно:

```text
--model
--language
--resume
```

`--dry-run` не делает API calls.

---

# 67. Example commands

Environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:GROQ_API_KEY="YOUR_KEY"
```

Check:

```bash
python scripts/00_check_environment.py
python scripts/01_snapshot_groq_models.py
```

Benchmark:

```bash
python scripts/02_validate_benchmark.py
python scripts/03_make_splits.py
```

Smoke test:

```bash
python scripts/04_run_pilot_generation.py --limit 10
```

Full pilot:

```bash
python scripts/04_run_pilot_generation.py --resume
```

Then:

```bash
python scripts/05_build_target_labels.py
python scripts/06_run_semantic_clustering.py
python scripts/07_build_features.py
python scripts/08_train_baselines.py
python scripts/09_train_dynamic_model.py
python scripts/10_evaluate_validation.py
```

---

# 68. Expected reports

После pilot создать:

```text
results/reports/pilot_report.md
```

Он должен содержать реальные:

- number of facts;
- successful requests;
- failures;
- requests/model;
- tokens/model;
- factual error rate;
- unresolved label rate;
- semantic judge agreement;
- basic AUROC baselines;
- runtime;
- estimated main cost in API requests/days.

---

# 69. Required figures

Для финальной работы автоматически генерировать минимум:

1. factual error rate by language;
2. factual error rate by model;
3. semantic entropy: correct vs incorrect;
4. mean entropy trajectories: correct vs incorrect;
5. ROC curve;
6. Precision-Recall curve;
7. calibration curve;
8. static vs dynamic performance;
9. cross-language heatmap;
10. cross-model generalization;
11. adaptive sampling tradeoff;
12. distribution of samples used by adaptive policy.

Все графики должны быть построены из saved result tables.

---

# 70. Required tables

Минимум:

```text
Table 1 — benchmark composition
Table 2 — evaluated models and generation settings
Table 3 — factual error rates
Table 4 — baseline comparison
Table 5 — proposed vs static
Table 6 — language-specific metrics
Table 7 — cross-language
Table 8 — cross-model
Table 9 — ablation
Table 10 — adaptive sampling
```

---

# 71. Scientific wording rules

Никогда автоматически не писать:

```text
"proved"
"solved hallucinations"
"universal"
"works for all LLMs"
```

если эксперимент этого не поддерживает.

Предпочитать:

```text
"в исследуемых моделях"
"наблюдалась ассоциация"
"метод показал..."
"результаты поддерживают гипотезу..."
"в пределах нашего benchmark..."
```

---

# 72. Limitations, которые нужно честно отчётить

Если остаются актуальными:

- только Groq-hosted models;
- ограниченное число model families;
- отсутствие token logprobs;
- semantic clustering partly depends on an LLM judge;
- benchmark ограничен EN/RU/KZ;
- factual questions predominantly short-answer;
- samples are not independent in a strict statistical sense;
- model versions can change on hosted API;
- Groq backend determinism is best-effort;
- translation equivalence may not be perfect.

---

# 73. Semantic judge bias control

Чтобы judge не сделал работу циклической:

1. judge не видит correct answer;
2. judge не решает factual correctness;
3. judge только группирует claims;
4. judge prompt fixed;
5. human validation subset обязателен;
6. lexical baselines оцениваются отдельно;
7. judge model и target models явно документируются.

---

# 74. API model version drift

Groq может обновить backend.

Поэтому сохранять:

```text
system_fingerprint
model ID
date
model snapshot
```

При существенной смене fingerprint в середине main:

- не удалять данные;
- отметить affected generations;
- провести sensitivity analysis, если доля существенна.

---

# 75. Main data-quality checks

Перед feature build:

```text
expected cases
actual cases
missing target generations
missing samples
duplicate responses
exact duplicate samples
API errors
empty responses
refusal responses
```

Не считать case complete, если нет полного sample set, кроме отдельного adaptive experiment.

---

# 76. Complete-case rule

Для основного fixed-5 experiment использовать case только если:

```text
1 target + 5 valid samples
```

доступны.

Incomplete cases:

- сохраняются;
- логируются;
- не маскируются;
- можно retry до завершения.

---

# 77. Response deduplication

Если stochastic generations иногда текстово идентичны — это **научный сигнал**, а не duplicate API row.

Не удалять одинаковые response texts.

Deduplication применяется только к повторно выполненному **тому же request key** после retry/resume.

---

# 78. Self-consistency vs correctness

Код и отчёт должны явно различать:

```text
consistency != correctness
```

Модель может:

```text
5/5 раз дать один и тот же неправильный ответ
```

Поэтому target factual correctness всегда определяется независимо через benchmark ground truth.

Это один из центральных научных моментов проекта.

---

# 79. Optional secondary experiment: confidence elicitation

Только если основной pipeline завершён.

Можно попросить target model после ответа дать self-reported confidence:

```text
0–100
```

и проверить, является ли она useful predictor.

Это отдельный baseline.

Не смешивать с core method без protocol amendment.

---

# 80. Demo

Делать только после final metrics.

Streamlit demo:

Input:

```text
Question
Language
Model
```

Output:

```text
Target answer
Sample answers
Semantic groups
Entropy trajectory
Consensus trajectory
Predicted factual-error risk
Number of samples used
```

Demo не должна выдавать risk score, если trained model artifact отсутствует.

Никаких fake demo values.

---

# 81. Demo API budget

Demo использует максимум:

```text
1 target + up to 5 samples + optional 1 semantic judge request
```

Показывать пользователю:

```text
requests used
model
sample count
```

---

# 82. Paper-ready artifacts

Скрипт:

```text
scripts/18_build_report.py
```

должен собрать:

```text
results/reports/final_results.md
```

с:

- experiment metadata;
- benchmark hash;
- model IDs;
- data counts;
- final metrics;
- confidence intervals;
- ablations;
- cross-language;
- cross-model;
- adaptive results;
- limitations.

Этот report является source of truth для написания научной работы.

---

# 83. STATUS.md

После каждой фазы обновлять:

```markdown
# Project Status

## Current phase
...

## Completed
- ...

## Tests
- ...

## Data generated
- ...

## Blockers
- ...

## Next exact command
...
```

---

# 84. CHANGELOG.md

Любое изменение научного протокола после первого pilot:

```text
date
change
reason
affected experiments
requires rerun: yes/no
```

---

# 85. Execution phases for Codex

---

## PHASE 0 — Repository bootstrap

### Tasks

- создать структуру;
- создать configs;
- dependencies;
- logging;
- `.env.example`;
- `STATUS.md`;
- basic tests.

### Definition of Done

```text
pytest passes
python scripts/00_check_environment.py works
```

Не делать генерации.

---

## PHASE 1 — Groq integration

### Tasks

- Groq client;
- model listing;
- model snapshot;
- retry;
- rate limiting;
- budget tracking;
- request persistence;
- dry-run mode.

### Definition of Done

Выполнить 3 тестовых Groq requests без потери metadata.

Сымитировать restart и доказать resume.

---

## PHASE 2 — Benchmark tooling

### Tasks

- Pydantic/schema validation;
- CSV validation;
- deterministic split;
- SHA-256;
- source checks.

### Definition of Done

Все benchmark/split tests проходят.

Не нужно сразу иметь 500 готовых facts, но pipeline должен быть готов.

---

## PHASE 3 — 10-fact smoke test

### Tasks

- 10 facts;
- 3 languages;
- 2 models;
- target + samples;
- raw persistence.

### Definition of Done

End-to-end generations complete.

No duplicate request keys.

---

## PHASE 4 — Labeling

### Tasks

- normalization;
- exact/alias/numeric/date;
- manual queue.

### Definition of Done

10-fact smoke dataset полностью получает factual labels или explicit unresolved status.

---

## PHASE 5 — Semantic grouping

### Tasks

- lexical features;
- semantic judge;
- JSON parsing;
- cache;
- clusters.

### Definition of Done

Все complete smoke cases получают cluster assignments.

---

## PHASE 6 — Dynamic feature pipeline

### Tasks

- static uncertainty;
- prefix trajectories;
- dynamic features;
- target support.

### Definition of Done

Manually inspect at least 5 cases and verify calculations.

All unit tests pass.

---

## PHASE 7 — Scientific pilot

### Tasks

- pilot dataset;
- Groq generations;
- factual labels;
- semantic grouping;
- judge validation;
- features;
- baselines;
- dynamic model.

### Definition of Done

`pilot_report.md` exists with real metrics and feasibility analysis.

---

## PHASE 8 — Protocol freeze

### Tasks

По pilot выбрать:

- exact sample count;
- feature set;
- classifier candidates;
- semantic thresholds;
- evaluation metric;
- main benchmark size.

Создать `FROZEN_CONFIG.yaml`.

### Definition of Done

Main experiment configuration immutable.

---

## PHASE 9 — Main generation

### Tasks

Запускать multi-day Groq requests resume-safe.

### Definition of Done

Все complete cases собраны либо exceptions документированы.

---

## PHASE 10 — Main labels + features

### Definition of Done

Final feature table generated.

Data-quality report generated.

---

## PHASE 11 — Train/validation model selection

### Definition of Done

Одна final proposed model выбрана на validation.

Threshold и calibration frozen.

---

## PHASE 12 — Test evaluation

### Definition of Done

Test metrics calculated once.

Bootstrap CIs generated.

Lock created.

---

## PHASE 13 — Cross-language / cross-model / ablation

### Definition of Done

Все experiment result CSV готовы.

---

## PHASE 14 — Adaptive sampling

### Definition of Done

Есть tradeoff между API request reduction и factual-error detection performance.

---

## PHASE 15 — Paper artifacts

### Definition of Done

Все final figures/tables/report generated directly from data.

---

## PHASE 16 — Demo

### Definition of Done

Streamlit demo uses real trained model and real Groq responses.

---

# 86. Agent behavior

Codex должен самостоятельно продолжать следующую фазу, если:

- предыдущая Definition of Done выполнена;
- нет scientific decision, требующего пользователя;
- нет отсутствующего API key;
- нет проблемы с Free Tier/model availability.

Codex должен остановиться и спросить пользователя, если:

1. требуемая Groq model недоступна;
2. main benchmark ещё не human-verified;
3. semantic judge validation проваливается;
4. pilot показывает почти нулевой factual error rate;
5. proposed dynamic features не имеют вариативности;
6. требуется изменить frozen protocol;
7. API key отсутствует;
8. необходимое действие может создать платные расходы.

---

# 87. Critical scientific fail conditions

Если pilot показывает:

```text
target factual error rate < ~5%
```

dataset слишком лёгкий.

Не начинать main.

Нужно увеличить difficulty / rare facts / false-premise subset.

Если:

```text
semantic entropy almost always 0
```

sampling protocol недостаточно разнообразен.

Не менять temperature хаотично.

Провести controlled pilot amendment.

Если semantic judge-human agreement низкий:

не использовать judge clusters как core feature до исправления.

---

# 88. Success criteria

Проект считается успешно реализованным, если:

1. есть >= 300 human-verified facts в main benchmark;
2. все факты имеют EN/RU/KZ versions;
3. исследованы >= 3 Groq target models, если доступность позволяет;
4. raw API outputs сохранены;
5. factual labels независимы от target LLM;
6. semantic uncertainty measured from repeated outputs;
7. dynamic features рассчитаны;
8. static vs dynamic comparison выполнен;
9. test set не использован для tuning;
10. bootstrap CI рассчитаны;
11. cross-language evaluation выполнена;
12. cross-model evaluation выполнена;
13. ablation выполнен;
14. adaptive sampling оценён;
15. все итоговые цифры воспроизводятся из saved data;
16. нет synthetic/fake results.

---

# 89. Minimal viable project

Если время резко ограничено, минимально допустимая научная версия:

```text
300 facts
3 languages
2 Groq target models
1 fixed Groq semantic judge
1 target + 5 samples
static + dynamic semantic uncertainty
Logistic Regression
AUROC/AUPRC
cross-language evaluation
bootstrap CI
```

Не тратить время на frontend.

---

# 90. Full target version

Желаемая версия:

```text
500 facts
3 languages
3 Groq target models
5 samples
human-validated semantic judge
static + dynamic features
cross-language
cross-model
ablation
calibration
adaptive sampling
final demo
```

---

# 91. First commands Codex should execute

После получения этого файла Codex должен:

```text
1. Inspect repository.
2. If repository is empty, create the structure from this plan.
3. Create STATUS.md.
4. Implement PHASE 0.
5. Run tests.
6. Implement PHASE 1.
7. Do NOT make Groq API calls until GROQ_API_KEY exists.
8. Once key exists, snapshot available models before selecting them.
9. Report actual available Free Tier target/judge model IDs.
10. Continue with PHASE 2.
```

---

# 92. Current preferred model configuration

Create initially:

```yaml
# configs/models.yaml

target_models:
  - id: openai/gpt-oss-20b
    enabled: true

  - id: qwen/qwen3.6-27b
    enabled: true

  - id: qwen/qwen3.8-27b
    enabled: true

semantic_judge:
  id: openai/gpt-oss-120b

availability_policy:
  verify_with_models_endpoint: true
  require_free_tier_access: true
  allow_silent_substitution: false
```

Do not assume availability solely from this file.

---

# 93. Initial generation config

```yaml
# configs/generation.yaml

prompt_version: factual_v1

target:
  temperature: 0.0
  seed: 42
  max_completion_tokens: 96

sampling:
  count: 5
  temperature: 0.7
  top_p: 0.95
  max_completion_tokens: 96
  seeds: [101, 202, 303, 404, 505]

semantic_judge:
  temperature: 0.0
  seed: 777
  max_completion_tokens: 256
```

---

# 94. Initial experiment config

```yaml
# configs/experiment.yaml

seed: 42

pilot:
  fact_count: 100

main:
  target_fact_count: 500
  minimum_fact_count: 300

splits:
  train: 0.70
  validation: 0.15
  test: 0.15

primary_metric: auroc

bootstrap:
  resamples: 1000
  confidence_level: 0.95

adaptive:
  min_samples: 2
  max_samples: 5
```

---

# 95. Final instruction to Codex

**Build the research infrastructure first.**

Do not optimize for visual polish.

Do not invent data.

Do not silently simplify the experiment.

Do not use paid inference.

Do not introduce local generative models.

Do not claim scientific novelty until literature review supports it.

Every result shown to the user must be traceable to:

```text
benchmark row
→ Groq raw response
→ factual label
→ semantic grouping
→ feature row
→ trained model
→ metric calculation
```

That traceability is mandatory.

---

# 96. Groq documentation references used when this plan was written

These URLs are reference material for the agent. Re-check them before the main experiment because API/model availability can change.

```text
https://console.groq.com/docs/api-reference
https://console.groq.com/docs/models
https://console.groq.com/docs/rate-limits
https://console.groq.com/docs/openai
https://console.groq.com/docs/deprecations
```

Key assumptions at protocol version 1.0:

- Groq Free Plan exists with model-specific limits.
- `n` is limited to 1 for chat completions, so repeated samples require separate requests.
- `logprobs/top_logprobs` are not currently supported by hosted chat models.
- `seed` is best-effort deterministic, not guaranteed.
- model availability can change; always snapshot `/models`.
