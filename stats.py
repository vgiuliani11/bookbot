def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in dict:
            dict[lower_char] = 1
        else:
            dict[lower_char] += 1
    return dict


def sort_on(dict):
    return dict["num"]


def get_sorted_dict_list(dict):
    list = []
    for key in dict.keys():
        if key.isalpha():
            list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list


def print_book_report(path):
    text = get_book_text(path)
    word_count = get_word_count(text)
    chars_dict = get_char_count(text)
    get_sorted_dict_list(chars_dict)
    char_sorted_list = get_sorted_dict_list(chars_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for dict in char_sorted_list:
        print(f"{dict['char']}: {dict['num']}")
    print("--- End report ---")
