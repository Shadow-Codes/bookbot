def count_words(content):
    return len(content.split())


def count_characters(content):
    lowercase_content = content.lower()
    char_dict = {}

    for char in lowercase_content:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict


def sort_dict(char_dict):
    char_list = list(map(lambda x: {"char": x[0], "count": x[1]}, char_dict.items()))
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list
