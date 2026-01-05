def word_count(input):
    count = len(input.split())
    return count
def char_count(input):
    c_count = {}
    for i in input:
        i = i.lower()
        if i not in c_count:
            c_count[i] = 1
        else:
            c_count[i] += 1
    return c_count

def sort_on(item):
    # item looks like {"char": "e", "num": 44538}
    return item["num"]

def dict_sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

