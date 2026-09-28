### Task 2.1: Write a function find_longest_word(words) that takes a list of strings and returns the longest word. If there are multiple words with the same maximum length, return the first one you encounter

def find_longest_word(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        else:
            continue
    return longest_word

def find_longest_word_max(words):
    return max(words,key=len)

print(find_longest_word(["apple", "banana", "cherry", "kiwi"]))
print(find_longest_word_max(["apple", "banana", "cherry", "kiwi"]))