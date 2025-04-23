from stats import get_num_words
from stats import get_num_char



def get_book_text(file_path):
    return file_path

def main():
    path_to_file = get_book_text("./books/frankenstein.txt")
    
    with open(path_to_file) as f:
        file_contents = f.read()

        word_count = get_num_words(file_contents)
        char_count = get_num_char(file_contents)
        
        # sorts, but turns dict into a list - so need .items to make a list of tuples that keep key:value pair
        sorted_char_count = sorted(char_count.items())

        # using dict method to turn back into a dictionary since we have key vlaue pairs
        sorted_dict = dict(sorted_char_count)
        print(sorted_char_count)
        print(sorted_dict)

main()

