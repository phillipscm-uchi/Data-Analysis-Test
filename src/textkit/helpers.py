"""Internal helpers."""
import re


def clean_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()
