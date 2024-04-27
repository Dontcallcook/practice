# Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).
# The function should ignore spaces, punctuation, and capitalization.
word1 = "hello    olleh"
word2 = "hello"

def palindrome_checker(word):
    cleaned_word = word.lower().strip(" .,!?-:;")
    char_list = []
    for char in cleaned_word:
        char_list.append(char)
    char_list_rev = char_list.copy()
    char_list_rev.reverse()
    if char_list == char_list_rev:
        return True
    return False

            


print(palindrome_checker(word1))
print(palindrome_checker(word2))