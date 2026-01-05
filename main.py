import sys
from stats import word_count, char_count, dict_sort

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = sys.argv[1]
    a = get_book_text(text)
    b = word_count(a)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}...")
    print("----------- Word Count ----------")
    print(f"Found {b} total words")
    print("--------- Character Count -------")
    char_counts = char_count(a)
    sorted_chars = dict_sort(char_counts)

    for item in sorted_chars:
        char = item["char"]
        num = item["num"]

        if not char.isalpha():
            continue
    
        print (f"{char}: {num}")
    print("============= END ===============")
main()