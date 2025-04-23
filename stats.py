def get_num_words(content):
    return content.split()


def get_num_char(content):
    ready_content = content.lower()
    letter_counts = {}
    for char in ready_content:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

