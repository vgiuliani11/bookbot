def main():
  path = "books/frankenstein.txt"
  text = get_book_text(path)
  word_count = get_word_count(text)
  print(f"There are {word_count} words found in the book.")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  words = text.split()
  return len(words)

main()