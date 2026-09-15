# Project status — 2026-09-15

## Завершено

- Benchmark: 100/100 фактов проверены человеком, EN/RU/KK.
- Generation: 5 400/5 400 ответов сохранены; наблюдались 900 target cases.
- Factual labels: 889 валидных target-ответов; 11 оборванных оставлены invalid.
- Semantic grouping: 866/866 полных случаев.
- Feature table: 832 строки после исключения 34 judge-uncertain случаев.
- Split: train 574, validation 127, locked test 131.
- Выбрана dynamic logistic, raw calibration, threshold 0.4015699460878933.
- Locked test открыт один раз.

## Locked-test результат

- Dynamic: AUROC 0.8791, AUPRC 0.6224, F1 0.4571, Brier 0.1030, ECE 0.0661.
- Static B4: AUROC 0.8415, AUPRC 0.4567, F1 0.3333.
- Paired ΔAUROC: +0.0376; 95% fact-bootstrap CI +0.0014…+0.0841.
- Paired ΔAUPRC: +0.1658; 95% CI +0.0469…+0.2741.

## Оставшийся научный этап

Очередь из 200 случаев для независимой human validation semantic judge подготовлена в `data/labels/pilot100_v1/semantic_review_queue.csv`. Эта проверка ещё не заявляется как завершённая.

## Релиз

Исследовательская работа, двуязычный дневник и презентация находятся в `deliverables/RKNP/`. Комплектность проверяется командой `python scripts/12_verify_release.py`.
