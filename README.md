# Прогнозирование фактических ошибок LLM

Исследовательский проект Саурыкова Ихсана Азаматовича, 12D, НИШ ФМН города Талдыкорган. Проект проверяет, помогает ли динамика семантической согласованности повторных ответов заранее находить фактические ошибки языковых моделей.

## Итог pilot100_v1

- 100 проверенных человеком фактов на английском, русском и казахском языках;
- 3 модели Groq, один target и 5 повторных генераций;
- 5 400 сохранённых ответов;
- 866 из 866 полных случаев прошли semantic grouping;
- 832 случая вошли в таблицу признаков;
- locked test: 131 случай, включая 24 фактические ошибки;
- dynamic logistic: AUROC 0,879, AUPRC 0,622;
- static comparator: AUROC 0,842, AUPRC 0,457;
- разница AUROC: +0,038, 95% bootstrap CI +0,001…+0,084.

Итоговые метрики находятся в `results/reports/pilot100_v1_test_metrics.json`, краткий отчёт — в `results/reports/pilot100_v1_final_results.md`.

## Что находится в репозитории

- `src/` — клиент Groq, журнал запросов, разметка, semantic judge, признаки, модели и метрики;
- `scripts/` — воспроизводимые этапы pipeline;
- `configs/` — параметры моделей и эксперимента;
- `data/benchmark/` — замороженный многоязычный benchmark;
- `data/labels/` — factual labels и очередь независимой semantic validation;
- `artifacts/features/`, `artifacts/models/`, `artifacts/predictions/` — итоговые научные артефакты;
- `artifacts/semantic_judgments/` — результаты semantic grouping;
- `results/` — отчёты и графики;
- `deliverables/RKNP/` — исследовательская работа, дневник и презентация;
- `IMPLEMENTATION_PLAN.md` и `RESEARCH_PROTOCOL.md` — исходный план и протокол.

API-ключи, SQLite-журналы запросов, логи и временные сборочные файлы в Git не добавляются.

## Быстрый локальный запуск на Windows

Требуется Python 3.12 и Git.

```powershell
git clone <URL-РЕПОЗИТОРИЯ>
cd rknp-factual-failure-dynamics
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.venv\Scripts\python.exe scripts/00_check_environment.py
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe scripts/12_verify_release.py
```

Последняя команда ничего не пересчитывает и не требует API-ключа. Она проверяет комплектность опубликованных данных и печатает показатели locked test.

## Запуск нового эксперимента через Groq

Создайте собственный ключ Groq и передайте его только через переменную окружения:

```powershell
$env:GROQ_API_KEY="ваш_ключ"
.venv\Scripts\python.exe scripts/01_snapshot_groq_models.py
.venv\Scripts\python.exe scripts/check_groq_integration.py --dry-run
```

Не записывайте ключ в конфиг, код или отслеживаемый файл. `.env.example` содержит только название переменной.

Полный порядок этапов:

```powershell
# 1. Benchmark и split по fact_id
.venv\Scripts\python.exe scripts/02_validate_benchmark.py --main --config configs/pilot100_v1.json --experiment-id pilot100_v1
.venv\Scripts\python.exe scripts/03_make_splits.py --config configs/pilot100_v1.json --experiment-id pilot100_v1

# 2. Target + пять samples; resume продолжает журнал без дублей
.venv\Scripts\python.exe scripts/04_run_pilot_generation.py --config configs/pilot100_provider_limits_v1.json --experiment-id pilot100_v1 --resume

# 3. Factual labels и очередь ручной проверки
.venv\Scripts\python.exe scripts/05_build_target_labels.py --config configs/pilot100_v1.json --experiment-id pilot100_v1
.venv\Scripts\python.exe scripts/prepare_target_review.py --config configs/pilot100_v1.json --experiment-id pilot100_v1

# 4. Semantic grouping и признаки
.venv\Scripts\python.exe scripts/06_run_semantic_clustering.py --config configs/pilot100_v1_semantic_primary.json --experiment-id pilot100_v1
.venv\Scripts\python.exe scripts/07_build_features.py --config configs/pilot100_v1.json --experiment-id pilot100_v1

# 5. Обучение и выбор только на validation
.venv\Scripts\python.exe scripts/08_train_baselines.py --config configs/pilot100_v1.json --experiment-id pilot100_v1
.venv\Scripts\python.exe scripts/09_train_dynamic_model.py --config configs/pilot100_v1.json --experiment-id pilot100_v1
.venv\Scripts\python.exe scripts/10_evaluate_validation.py --config configs/pilot100_v1.json --experiment-id pilot100_v1

# 6. Однократное открытие закрытого test
.venv\Scripts\python.exe scripts/11_evaluate_test_once.py --config configs/pilot100_v1.json --experiment-id pilot100_v1
```

Для нового научного запуска используйте новый `experiment-id` и отдельные versioned paths. Test-скрипт специально отказывается перезаписывать уже полученный результат.

## Человеческая разметка

Factual labels оценивают весь target-ответ. Оборванные ответы не превращаются автоматически в фактические ошибки. Результаты semantic judge не считаются человеческой истиной: в `data/labels/pilot100_v1/semantic_review_queue.csv` находится слепая стратифицированная выборка из 200 случаев для независимой проверки.

## Воспроизводимость

- seed: 42;
- split: 70/15/15 на уровне фактов;
- target: temperature 0, seed 42;
- samples: temperature 0,7, top-p 0,95, seeds 101/202/303/404/505;
- semantic prefixes: k=2, 3, 4, 5;
- bootstrap: 1 000 повторов на уровне `fact_id`;
- модель, calibration и threshold выбраны до открытия test.

Исследование является pilot на 100 фактах. Главным оставшимся ограничением является независимая человеческая проверка 200 semantic-grouping случаев.
