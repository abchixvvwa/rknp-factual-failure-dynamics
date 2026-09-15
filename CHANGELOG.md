# Changelog

## 2026-09-12 — Resumed pilot and prepared partial human review
- Resumed pilot100_v1 after cooldown, reusing all 3,004 previously stored responses.
- Built factual-label preparation for the first 50 facts: 98 resolved automatically, 352 awaiting human review, 434 complete cases out of 450.
- Added immutable numbered review snapshots with exact request/response hashes and source links; produced eight batches and verified their mapping and completeness. No review labels were fabricated.

## 2026-09-11 — User-authorized provider-only throughput
- Disabled local throttling in a versioned operational config, retaining provider cooldowns, 429 retry handling and usage accounting. Defaults now select provider-only mode; historical resolved configs remain unchanged.
- Preserved pilot questions, sampling parameters, request identity and original freeze. Resume uses pilot100_provider_limits_v1.json with the same pilot100_v1 ID.
- 67 tests pass. At restart, 320 pilot responses were persisted and no requests were in flight.

## 2026-09-11 — Pilot verified, frozen and launched
- Recorded explicit user confirmation of all 76 remaining facts, sources, aliases and languages. Applied pilot_025 KK, pilot_030 KK and pilot_036 RU edits; retained pilot_032 Афина.
- Saved a separate 100-row verified dataset, review audit, final config and frozen 70/15/15 pilot assignments with hashes; historical candidate data remains intact.
- Real pilot100_v1 generation started under the existing 900-request daily ceiling. No scientific metrics yet.

## 2026-09-11 — Full pilot candidates prepared
- Added 76 primary-source-backed candidates and a readable EN/RU/KK review document; all new facts remain human-unverified. Preserved the 24 reviewed facts unchanged.
- Assembled 100 candidates with the planned category quotas; recorded source-access and topical-concentration limitations, hashes and an unfrozen split preview.
- Added a pre-request human-verification gate and its no-API-call regression test. All 66 tests pass.
- Generation planning dry run reports 5,400 target/sample requests; no inference or scientific metrics were produced.

## 2026-09-11 — User review imported
- Imported 45 numbered factual decisions by matching the review document's request IDs and response hashes: 36 correct, 9 incorrect. Preserved the submission and previous labels/features in data/reviews/user_review_2026-09-11/.
- Rebuilt all 60 target labels and 59 complete feature rows; no unresolved labels remain. No scientific training or new Groq inference was run.
- Created pilot_verified_v1.csv for the 24 user-confirmed facts with requested source and Kazakh wording changes. Five corrected Nobel summary URLs returned 403 to the agent; this is recorded, not treated as independent source verification.
- Enabled user-reviewed factual_v1_kk for future requests; retained old factual_v1 for reproducibility. Semantic grouping validation remains pending.
- 65 tests pass, including preservation of historical prompts and rejection of unknown prompt versions.

## 2026-09-11 — Training preparation and sourced candidates
- Implemented six baselines, three dynamic classifiers, fact-grouped train-only calibration and validation model/threshold selection (scripts 08–10).
- Test values are not loaded during development; model/feature hashes protect selection and output files cannot be overwritten.
- Real smoke training dry run correctly refuses the ten-fact dataset. All training outputs so far are temporary unit-test fixtures, not scientific evidence.
- Prepared 24 source-backed EN/RU/KK pilot candidates, four per category, with a separate human-review document. All remain unverified; 76 more pilot facts are still needed.
- Updated actual smoke status: 59 complete semantic cases, 59 feature rows, five arithmetic checks; human judge agreement remains unmeasured.

## 2026-09-10 — Initial implementation
- Preserved protocol v1 from the supplied plan. No pilot has run and no scientific protocol amendments have been made.
- Repository root is the current workspace (no redundant nested repository).
- SQLite is the crash-safe canonical request journal; Parquet is a derived checkpoint/export.
- User explicitly confirmed the organization uses Groq Free Plan. This is not inferred from model listing.
- Operational daily cap starts at 100 requests across this project; account limits still apply independently.

## 2026-09-10 — Pre-pilot amendment 1
- Evidence: integration_v1 Qwen 3.6 used all 96 completion tokens for reasoning and returned finish_reason=length; the other two models returned OK.
- User authorized selecting the best correction. Both Qwen models now explicitly use reasoning_effort=none; the 96-token output ceiling stays unchanged.
- Affected experiments: new integration_v2 and subsequent smoke/pilot only. Original integration_v1 remains unchanged.
- Requires rerun: yes, integration under the new parameters. No scientific pilot or main results exist.
- Operational daily project cap raised from 100 to 900 to accommodate the 360-request engineering smoke run; per-model request/token ceilings remain enforced.
- Input estimation overhead increased to 128 after the transport check showed model-added prompt overhead.

## 2026-09-10 — Pre-pilot amendment 2
- Evidence: smoke_v1 stopped after 10 requests when Qwen 3.8 sample 3 on smoke_001 emitted a factual explanation that exceeded 96 tokens despite reasoning_effort=none. GPT OSS samples also used 71–94 tokens including reasoning.
- Under the user's authorization to choose the best correction, raise the completion ceiling to 512 for targets and samples on all models. Prompts, temperatures, top_p and seeds remain fixed. This is a ceiling, not a required answer length.
- Affected experiments: new smoke_v2 and later pilot. Requires rerun: yes. Preserve all 10 smoke_v1 responses, including the truncated response.

## 2026-09-10 — Pre-pilot amendment 3 and human verification
- smoke_v2 stopped after 30 outputs: GPT OSS 20B used 510 reasoning tokens while translating a month into Kazakh, then returned empty content at the 512-token ceiling.
- Explicit reasoning_effort=low for GPT OSS 20B and the fixed 120B judge; keep the uniform target/sample ceiling at 512. Requires rerun: yes, smoke_v3. No scientific result selection has occurred.
- User explicitly confirmed all 10 smoke facts, sources and EN/RU/KK questions were checked. Saved facts_verified_v1.csv and human_verification.json; the original running datasets remain unchanged.
- This confirmation covers only the 10 listed fact IDs, not future facts, generated target labels or semantic judge annotations.

## 2026-09-10 — Smoke exception handling
- smoke_v3 encountered one looping Kazakh Qwen 3.8 sample at the 512-token ceiling after 249 stored responses.
- Do not retune token ceilings to erase this behavior. Continue the queue, retain the invalid response and exclude its case from fixed-five features under the original complete-case rule (§76).
- Scientific generation parameters unchanged; no rerun of successful responses. Quality reports must show exclusions and their language/model distribution.
- Fixed transient Windows progress-file replacement failures with bounded retries; a real restart skipped 242 existing responses without duplicating API calls.

## 2026-09-10 — Semantic output schema correction
- semantic_v1_prefix omitted answer C in a five-answer partition; validation rejected it. All 22 v1 API responses and completed case files are preserved.
- semantic_v2_prefix uses Groq strict JSON Schema with one required integer assignment per visible answer, converted into the documented groups representation after validation. Target support uses a required nullable group ID.
- Requires rerun: semantic judgments only, under a versioned directory and cache key. Target/sample generations are unchanged. This does not establish human agreement with the judge; that check is still required.

## 2026-09-10 — Groq structured response diagnostic
- semantic_v2_prefix received HTTP 400/tool_use_failed: the judge emitted a function-call wrapper instead of a direct structured answer. The request was recorded and was not retried blindly.
- semantic_v3_prefix explicitly prohibits tool/function wrappers and names the response schema `response`; retains strict per-answer assignments and independent prefix grouping. Earlier judgments remain separate.
- Requires rerun: semantic stage only; generation data and factual labels unchanged.

## 2026-09-10 — Bounded semantic truncation recovery
- After 53 completed v3 case files, one judge response reached the 256-token ceiling.
- On finish_reason=length only, allow one explicitly recorded judge request with the same model/prompt/seed and a 1024-token ceiling. Original output stays preserved; the retry has a distinct request hash and audit link.
- Completed judgments are reused. The engineering set can contain both judge token ceilings, recorded per judgment and in the semantic manifest. This is not selection based on correctness or test performance.
- Target/sample requests remain unchanged. Any later scientific freeze must include this retry policy or adopt a fixed ceiling before new data collection.
