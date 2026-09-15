# Технический отчёт: pilot100_v1

Это engineering smoke, а не научный pilot. Метрики классификатора не рассчитывались.

Сохранено ответов: 5400. Полных случаев: 866 из 900. Непригодных ответов: 48. Повторяющихся request keys: 0.

SHA-256 benchmark: `df2c36a8ac136194e654ba11d018d851cadcb9e48dc28578eaceb40143560ce6`.

## Реальный расход Groq

| Model | Requests | Input tokens | Output tokens |
|---|---:|---:|---:|
| openai/gpt-oss-20b | 1800 | 257706 | 124550 |
| qwen/qwen3.6-27b | 1800 | 183060 | 55076 |
| qwen/qwen3.8-27b | 1800 | 183060 | 89220 |

## Неполные случаи

- pilot_013, kk, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_013, ru, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_014, kk, qwen/qwen3.8-27b: 2/5 пригодных samples.
- pilot_016, en, openai/gpt-oss-20b: 4/5 пригодных samples.
- pilot_016, kk, qwen/qwen3.6-27b: 3/5 пригодных samples.
- pilot_016, kk, qwen/qwen3.8-27b: 3/5 пригодных samples.
- pilot_016, ru, openai/gpt-oss-20b: 4/5 пригодных samples.
- pilot_016, ru, qwen/qwen3.6-27b: 3/5 пригодных samples.
- pilot_016, ru, qwen/qwen3.8-27b: 5/5 пригодных samples.
- pilot_019, en, openai/gpt-oss-20b: 4/5 пригодных samples.
- pilot_019, kk, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_021, en, qwen/qwen3.6-27b: 4/5 пригодных samples.
- pilot_021, kk, qwen/qwen3.8-27b: 5/5 пригодных samples.
- pilot_021, ru, qwen/qwen3.8-27b: 5/5 пригодных samples.
- pilot_022, kk, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_046, kk, openai/gpt-oss-20b: 4/5 пригодных samples.
- pilot_062, kk, qwen/qwen3.6-27b: 3/5 пригодных samples.
- pilot_070, kk, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_076, kk, qwen/qwen3.6-27b: 4/5 пригодных samples.
- pilot_076, kk, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_082, kk, openai/gpt-oss-20b: 4/5 пригодных samples.
- pilot_083, en, openai/gpt-oss-20b: 5/5 пригодных samples.
- pilot_084, kk, qwen/qwen3.6-27b: 4/5 пригодных samples.
- pilot_084, kk, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_085, kk, openai/gpt-oss-20b: 4/5 пригодных samples.
- pilot_085, kk, qwen/qwen3.8-27b: 3/5 пригодных samples.
- pilot_085, ru, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_086, kk, openai/gpt-oss-20b: 3/5 пригодных samples.
- pilot_086, ru, openai/gpt-oss-20b: 4/5 пригодных samples.
- pilot_086, ru, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_087, en, openai/gpt-oss-20b: 5/5 пригодных samples.
- pilot_087, ru, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_088, kk, qwen/qwen3.8-27b: 4/5 пригодных samples.
- pilot_088, ru, qwen/qwen3.8-27b: 4/5 пригодных samples.

Сбои сохранены и исключены из fixed-five анализа; они не подменены фактическими ошибками. Потеря случаев может зависеть от языка и модели и должна учитываться в ограничениях исследования.
