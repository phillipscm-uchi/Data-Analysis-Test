from textkit import slugify, word_count, truncate, is_palindrome


def test_slugify():
    assert slugify("Héllo, World!") == "hello-world"


def test_word_count():
    assert word_count("a  b\nc") == 3


def test_truncate():
    assert truncate("abcdefghij", 6) == "abc..."


def test_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
