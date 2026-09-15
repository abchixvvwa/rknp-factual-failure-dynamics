# Benchmark

`facts.csv` currently contains **10 engineering smoke facts**, not a scientific pilot or main benchmark.
Questions and aliases have EN/RU/KK coverage; all verification flags in this original file remain **false**.
The user subsequently confirmed all ten facts, sources and translations. The reviewed version is
`facts_verified_v1.csv` with all ten flags **true**; `human_verification.json` records that confirmation
and both hashes. `configs/smoke_v3.json` selects it. Future facts are not covered by this confirmation.
The agent consulted the authoritative URLs on 2026-09-10. A human must check factual accuracy,
alias sufficiency, question equivalence and the Kazakh prompt before main; do not bulk-set verification flags.
The UN page was available through the search index but direct retrieval failed; review it manually.

The smoke set intentionally contains easy facts to test infrastructure. It cannot establish classifier performance.
Mercury facts share a subject and the two moon questions share a template; these correlations must be considered
when constructing the independent scientific benchmark. Pilot/main require a separate versioned dataset.

Schema: one row per unique fact_id, with three question fields, independent canonical answer,
JSON list of aliases, authoritative source URL/title/publisher/access date, and human verification flag.
Category counts: history 2, geography 2, science 2, culture 1, Kazakhstan 1, false premise 2.
Question types in this engineering set: entity, numeric, date, false_premise; add direct_fact coverage for pilot.

Run `python scripts/02_validate_benchmark.py` and `python scripts/03_make_splits.py`.
`--main` deliberately rejects this unverified set. `--check-sources` checks reachability only.
Write new benchmark/split paths in a separate config for pilot/main; do not overwrite a started experiment.

Research source references are embedded in every CSV row; there are no generated or invented source URLs.
