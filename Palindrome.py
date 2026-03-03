
word = input("What is your word?")

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

if palindrome(word):
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")
