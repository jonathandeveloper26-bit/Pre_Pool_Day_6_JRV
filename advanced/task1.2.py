"Task 1.2: Write a recursive function reverse_string(text) that takes a string of characters and returns it completely backwards."

def reverse_string(text):
    rev_string = ""
    if len(text) <= 1: 
        return text
    else:
        rev_string = text[-1] + reverse_string(text[0:len(text)-1])
    return rev_string

print(reverse_string("Epitech"))