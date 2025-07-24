from stats import count_words
from stats import count_characters
from stats import report
import sys


def get_book_text(file):
    with open(file) as f:
        contents = f.read()
        return contents


def format_word_count(num_words):
    return f"Found {num_words} total words"


def main():
    #book1 = "books/frankenstein.txt" hardcoded for original testing
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book1 = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book1}")
        print("----------- Word Count ----------")
        print(format_word_count(
            count_words(get_book_text(book1))))
        print("--------- Character Count -------")
        characterCount = count_characters(get_book_text(book1))
        #print(characterCount)
        myReport = report(characterCount)
        for rep in myReport:
            if rep["char"].isalpha():
                print(f"{rep["char"]}: {rep["num"]}")
            else:
                continue
        print("============= END ===============")

main()
