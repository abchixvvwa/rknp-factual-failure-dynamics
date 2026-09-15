# RKNP pilot100_v1 — final locked-test results

## Protocol

- 100 source-backed facts; EN/RU/KK; three Groq-hosted target models.
- 900 fact-language-model cases, 866 complete 1+5 cases.
- 832 feature-bearing cases after excluding 34 incomplete and 34 judge-uncertain cases.
- Fact-level train/validation/test split; model and threshold selected on validation only.
- Locked test opened once; 1,000 fact-level bootstrap resamples.

## Selected model

`dynamic_logistic`, raw calibration, validation-selected threshold `0.401570`.

## Locked test

| Metric | Dynamic | Static comparator |
|---|---:|---:|
| AUROC | 0.879 | 0.842 |
| AUPRC | 0.622 | 0.457 |
| F1 | 0.457 | 0.333 |
| Precision | 0.727 | 0.500 |
| Recall | 0.333 | 0.250 |
| Brier | 0.103 | 0.120 |
| ECE | 0.066 | 0.070 |

Dynamic AUROC 95% CI: `0.817–0.934`.  
Dynamic AUPRC 95% CI: `0.365–0.782`.  
Paired dynamic−static ΔAUROC 95% CI: `0.001–0.084`.  
Paired dynamic−static ΔAUPRC 95% CI: `0.047–0.274`.

The pilot supports the prespecified hypothesis within this benchmark: dynamic trajectory features improved discrimination over the static comparator. Recall at the validation-selected max-F1 threshold was 0.333, so the current model is more suitable for ranking/auditing than for automatically rejecting answers.

## Language slices

| Language | n | Errors | AUROC | AUPRC |
|---|---:|---:|---:|---:|
| EN | 45 | 7 | 0.944 | 0.712 |
| RU | 44 | 8 | 0.799 | 0.561 |
| KK | 42 | 9 | 0.892 | 0.703 |

## Limitations and gate

- Test has 131 cases and 24 factual errors; subgroup estimates are exploratory.
- Science has no positive test errors, so category AUROC is undefined there.
- Semantic grouping depends partly on a fixed LLM judge.
- The independent 200-case blinded human semantic review remains required before claiming validated judge reliability.
