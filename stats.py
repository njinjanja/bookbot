def count_words(booktext):
    number_of_words=booktext.split()
    return len(number_of_words)

def count_char_appearance(booktext):
    booktext = booktext.lower()
    char_dict={}
    for chara in booktext:
        if chara in char_dict:
            char_dict[chara] += 1
        else:
            char_dict[chara] = 1
    return char_dict
