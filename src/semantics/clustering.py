from src.labeling.normalize import normalize
from src.labeling.numeric_match import parse_number
from src.labeling.date_match import parse_date


def equivalence(a, b):
    if normalize(a) == normalize(b):
        return True
    for parse in (parse_number, parse_date):
        left, right = parse(a), parse(b)
        if left is not None and right is not None:
            return left == right
    return None


def deterministic_groups(answers):
    """Return None when any needed equivalence decision needs a semantic judge."""
    groups = []
    for index, answer in enumerate(answers):
        found = None
        for group in groups:
            same = equivalence(answer, answers[group[0]])
            if same is None:
                return None
            if same:
                found = group
                break
        if found is None:
            groups.append([index])
        else:
            found.append(index)
    return groups


def validate_groups(value, count):
    if not isinstance(value, dict) or type(value.get("uncertain")) is not bool:
        raise ValueError("Judge JSON requires boolean uncertain")
    groups = value.get("groups")
    if not isinstance(groups, list) or not groups:
        raise ValueError("Judge JSON requires nonempty groups")
    expected = {chr(65+i): i for i in range(count)}
    result, ids = [], set()
    for group in groups:
        if not isinstance(group, dict) or type(group.get("group_id")) is not int or group["group_id"] in ids:
            raise ValueError("Each group needs a distinct integer group_id")
        ids.add(group["group_id"])
        members = group.get("members")
        if not isinstance(members, list) or not members or any(not isinstance(m, str) or m not in expected for m in members):
            raise ValueError("Invalid group member")
        result.append(sorted(expected[m] for m in members))
    flattened = [index for group in result for index in group]
    if sorted(flattened) != list(range(count)):
        raise ValueError("Each answer must appear exactly once")
    return sorted(result, key=lambda group: group[0]), value["uncertain"]
