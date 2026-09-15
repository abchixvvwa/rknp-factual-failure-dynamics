import re
from datetime import date

from src.labeling.normalize import normalize

MONTHS = {}
for index, names in enumerate([
    "january января қаңтар", "february февраля ақпан", "march марта наурыз",
    "april апреля сәуір", "may мая мамыр", "june июня маусым", "july июля шілде",
    "august августа тамыз", "september сентября қыркүйек", "october октября қазан",
    "november ноября қараша", "december декабря желтоқсан",
], 1):
    MONTHS.update({word: index for word in names.split()})


def parse_date(text):
    text = normalize(text)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        try:
            return date.fromisoformat(text)
        except ValueError:
            return None
    text = re.sub(r"\b(?:года|жылғы)\b", "", text).replace(",", " ")
    parts = text.split()
    if len(parts) != 3:
        return None
    try:
        if parts[0] in MONTHS:
            month, day, year = MONTHS[parts[0]], int(parts[1]), int(parts[2])
        elif parts[1] in MONTHS:
            day, month, year = int(parts[0]), MONTHS[parts[1]], int(parts[2])
        elif parts[2] in MONTHS:
            year, day, month = int(parts[0]), int(parts[1]), MONTHS[parts[2]]
        else:
            return None
        return date(year, month, day) if 1000 <= year <= 9999 else None
    except ValueError:
        return None


def date_match(response, canonical):
    left, right = parse_date(response), parse_date(canonical)
    return None if left is None or right is None else left == right
