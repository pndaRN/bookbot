def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    words = text.lower()
    char = words.replace(" ","")
    char_count = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
    }
    for c in char:
        for alp in char_count:
            if c == alp:
                char_count[alp] += 1
    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse = True, key = sort_on)
    return char_list
