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

def sort_on(dictionary):
    return dictionary["num"]

def sort_dict(unsorted_dict):
    sorted_list=[]
    for key in unsorted_dict:
        count = unsorted_dict[key]
        char_dict = {"char":key, "num":count}
        sorted_list.append(char_dict)   
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list