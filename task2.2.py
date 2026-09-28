### Write a recursive function that prompts the user for a string of characters, strips out the spaces and punctuation signs, lowercases the string, then tests if it is a palindrome

def check_palindrome(string = "", user_input = True):

    if user_input == True: 
        string = input("Enter a String: ").lower()
        string.replace(" ", "")
        string.replace(".", "")
        string.replace("!", "")
        string.replace("?","")

    if len(string) <= 1:
        return True
    else:
        if (string[0] == string[-1]):
            check_palindrome(string = string[1:-1], user_input=False)
        else:
            return False
    return True

print("*"*30)
print("Task 2: Recursive Function to Test Palindromes")
print(check_palindrome())
print("*"*30)

