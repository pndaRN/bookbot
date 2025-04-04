from stats import get_num_words
from stats import get_num_char
from stats import sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    words = get_book_text(file_path)
    num = get_num_words(words)
    char_num = get_num_char(words)
    char_num_list = sort_dict(char_num)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")

    for char in char_num_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
            
main()