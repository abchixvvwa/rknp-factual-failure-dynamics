import re
import unicodedata


def normalize(text):
    text = unicodedata.normalize("NFKC", text).casefold()
    text = text.replace("−", "-").replace("–", "-").replace("—", "-")
    # Preserve signs, decimal separators and percent: -5 must never match 5.
    text = "".join(c if not unicodedata.category(c).startswith("P") or c in "-.,%" else " " for c in text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.rstrip(".,").strip()
