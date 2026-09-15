from itertools import combinations

from rapidfuzz.fuzz import ratio

from src.labeling.normalize import normalize


def lexical_features(answers):
    values = [normalize(a) for a in answers]
    pairs = list(combinations(values, 2))
    ratios = [ratio(a, b)/100 for a, b in pairs]
    jaccards = [len(set(a.split()) & set(b.split()))/max(1, len(set(a.split()) | set(b.split()))) for a, b in pairs]
    return dict(mean_pairwise_token_jaccard=sum(jaccards)/len(jaccards) if pairs else 1.0,
                mean_pairwise_rapidfuzz_ratio=sum(ratios)/len(ratios) if pairs else 1.0,
                min_pairwise_rapidfuzz_ratio=min(ratios, default=1.0),
                lexical_diversity=len(set(values))/len(values), normalized_answer_unique_count=len(set(values)))
