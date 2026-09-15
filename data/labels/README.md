# Human review

Benchmark verification is separate from labeling generated answers and assessing semantic judge reliability.
Confirming the ten benchmark rows does not provide either of these annotations.

## Factual targets

Run `05_build_target_labels.py` for the experiment. Its `manual_review_queue.csv` contains only unresolved targets.
Copy reviewed rows to top-level `reviewed_labels.csv`, retain `request_id` and `response_sha256`, and fill:

- `review_label`: `1` for factually correct, `0` for factually incorrect; blank means unresolved.
- `reviewer`: who completed the review.
- `review_notes`: explanation and relevant source details.

Re-run labeling. A hash mismatch or duplicate request ID is rejected. Review files are never automatically
filled by a generative model. A response with extra explanatory text is conservatively unresolved unless
the full response matches an explicit alias; an answer substring is insufficient evidence of correctness.
For false-premise questions, assess whether the premise is explicitly rejected, not just whether a familiar entity appears.

## Semantic judge validation

Run `prepare_semantic_review.py`. It requires 200 complete cases for scientific validation. A smaller
`--smoke-preview` queue is for engineering only. The queue intentionally hides judge groups and ground truth.
Fill `human_groups_json` as a five-element label list, for example `[0,1,0,0,2]`, plus reviewer and notes.
Label IDs have no meaning; only which answers share a factual claim matters. Do not judge which claim is correct.
Never overwrite an in-progress human review queue when resuming generation.
After annotation, run `validate_semantic_reviews.py` with the same experiment/config (and `--smoke-preview`
for the 59-case engineering set). It computes ARI, pairwise agreement and exact partition agreement from
saved data, rejecting empty/incomplete annotations. A report never automatically certifies the judge.
The report also compares each prefix against the corresponding restriction of the human five-answer partition,
so a correct final grouping does not hide unstable early judge decisions.
