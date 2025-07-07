from stats import count_words
from stats import count_char_appearance
from stats import sort_dict
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    book1 = get_book_text("books/frankenstein.txt")
    word_count = count_words(book1)
    dict_of_book=count_char_appearance(book1)
    sorted= sort_dict(dict_of_book)



    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')


    print("============= END ===============")

    # print(f"{word_count} words found in the document")
    # print(f"{dict_of_book}")
    # print(get_book_text("books/frankenstein.txt"))
main()