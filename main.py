def main():
    book_path = "books/frankenstein.txt"
    text = get_book_txt(book_path)
    num_of_words = word_count(text)
    
    char_dict = get_chars_dict(text)
    char_report_var = char_report(char_dict)
    
    print(f"--- Begin repot of {book_path} ---")
    print(f"{num_of_words} words found in the document")
    print()


    for item in char_report_var:
        if not item["char"].isalpha():
            continue # skips the rest of the loop if the item is non alphabetical
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_book_txt(path):
    with open(path) as f:
        return f.read()
        
def word_count(text):
    words = text.split()
    return len(words)
        

def get_chars_dict(text):
    chars = {} 
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict_item):
    return dict_item["num"]

def char_report(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



    

main()
