import re
import unicodedata
from decimal import Decimal, InvalidOperation


def parse_number(text):
    text = unicodedata.normalize("NFKC", text).strip().replace("−", "-")
    if re.fullmatch(r"[+-]?\d{1,3}(?:[ \u00a0\u202f]\d{3})+(?:\.\d+)?", text):
        text = re.sub(r"[ \u00a0\u202f]", "", text)
    # A single comma with three trailing digits is ambiguous: 1,234 is not auto-labeled.
    if re.fullmatch(r"[+-]?\d+,\d{1,2}", text):
        text = text.replace(",", ".")
    if not re.fullmatch(r"[+-]?\d+(?:\.\d+)?", text):
        return None
    try:
        return Decimal(text)
    except InvalidOperation:
        return None


def numeric_match(response, canonical):
    left, right = parse_number(response), parse_number(canonical)
    return None if left is None or right is None else left == right
