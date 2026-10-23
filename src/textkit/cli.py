import sys
from text_utils import slugify, word_count


def main():
    if len(sys.argv) < 3:
        print("usage: python cli.py [slug|count] TEXT")
        return
    cmd, text = sys.argv[1], " ".join(sys.argv[2:])
    print(slugify(text) if cmd == "slug" else word_count(text))


if __name__ == "__main__":
    main()
