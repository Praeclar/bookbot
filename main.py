
def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

        generate_report(file_contents)

def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")

    #word count
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    print("")

    #char count
    char_dict = count_chars(text, True)

    for char in char_dict:
        print(f"The '{char["char"]}' character was found {char["char_count"]} times")

    print("--- End report ---")

def count_words(text):
    words = text.split()
    word_count = len(words)

    return word_count

def sort_on(dict):
    return dict["char_count"]

def count_chars(text, sorted = False):
    char_counter = {}

    lowered_text = text.lower()

    for char in lowered_text:
        if(not char.isalpha()):
            continue

        if(char not in char_counter):
            char_counter[char] = 1
        else:
            char_counter[char] += 1

    char_list = []
    for char, char_count in char_counter.items():
        char_list.append({"char":char, "char_count":char_count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list
    

main()