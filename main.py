import sys

from stats import count_characters, count_words, sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()

    return content


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")

    filepath = sys.argv[1]

    content = get_book_text(filepath)
    word_count = count_words(content)
    sorted_counts = sort_dict(count_characters(content))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_counts:
        char, count = item["char"], item["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
