def main():
  path = "books/frankenstein.txt"
  text = get_book_text(path)
  word_count = get_word_count(text)
  chars_dict = get_char_count(text)
  print(f"There are {word_count} words found in the book.")
  print("Character count:")
  print(chars_dict)

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

main()
