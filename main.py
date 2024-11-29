def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    word_count = get_word_count(text)
    character_count = get_character_count_dict(text)
    list_of_dict = []

    for k, v in character_count.items():
        char_dict = {"char": k, "count": v}
        list_of_dict.append(char_dict)

    list_of_dict.sort(key=sort_on, reverse=True)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in list_of_dict:
        character = item["char"]
        char_count = item["count"]
        print(f"The '{character}' character was found {char_count} times")

    print(f"--- End report ---")


def get_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count_dict(string):
    lowered_string = string.lower()
    character_count = {}

    for char in lowered_string:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    return character_count


def sort_on(dict):
    return dict["count"]


main()
