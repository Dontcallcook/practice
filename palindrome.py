# Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).
# The function should ignore spaces, punctuation, and capitalization.

word1 = "hello olleh"
word2 = "hello"

def palindrome_checker(word):
    cleaned_word = word.lower().strip(" .,!?-:;")
    word_len = len(cleaned_word)
    start_index = 0
    end_index = word_len - 1
    
    while start_index < end_index:
        if cleaned_word[start_index] == cleaned_word[end_index]:
            start_index += 1
            end_index -= 1
        if cleaned_word[start_index] != cleaned_word[end_index]:
            return False
    return True

print(palindrome_checker(word1))
print(palindrome_checker(word2))