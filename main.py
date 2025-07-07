from stats import count_words
from stats import count_char_appearance

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    book1 = get_book_text("books/frankenstein.txt")
    word_count = count_words(book1)
    print(f"{word_count} words found in the document")
    dict_of_book=count_char_appearance(book1)
    print(f"{dict_of_book}")
    #print(get_book_text("books/frankenstein.txt"))
main()