from src.labeling.normalize import normalize


def exact_match(response, canonical, aliases=()):
    value = normalize(response)
    return bool(value) and value in {normalize(x) for x in [canonical, *aliases]}
