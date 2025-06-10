import sys
from stats import count_characters, count_words, create_list

def get_book_text(filename):
  print(f"Analyzing book found at {filename}...")
  with open(filename) as f:
    return f.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  print("============ BOOKBOT ============")
  book_text = get_book_text(sys.argv[1])
  print("----------- Word Count ----------")
  num_words = count_words(book_text)
  print(f"Found {num_words} total words")

  dictionary = count_characters(book_text)
  list = create_list(dictionary)

  print("--------- Character Count -------")

  for dictionary in list:
    if not dictionary['char'].isalpha():
      continue
    print(f"{dictionary['char']}: {dictionary["num"]}")

  print("============= END ===============")

main()
