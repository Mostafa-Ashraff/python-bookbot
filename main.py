def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counted_chars = get_count_of_each_char(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"the book has {num_words} words")
    for key in counted_chars:
        print((f"The '{key}' character was found {counted_chars[key]} times"))
    print("--- End report ---")
    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_of_each_char(text):
    lowercased_text = text.lower()
    counting_obj = {}
    for i in lowercased_text:
        if counting_obj.get(i):
            counting_obj[i] += 1
        else: 
            counting_obj[i] = 1
    return counting_obj    


main()