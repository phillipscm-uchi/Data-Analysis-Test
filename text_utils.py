"""Small text helpers."""
import re
import unicodedata
from helpers import clean_whitespace  # NOTE: works only when run from this folder


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def word_count(text):
    return len(clean_whitespace(text).split())


def truncate(text, length=50, suffix="..."):
    if len(text) <= length:
        return text
    return text[: length - len(suffix)].rstrip() + suffix


def is_palindrome(text):
    chars = [c.lower() for c in text if c.isalnum()]
    return chars == chars[::-1]
