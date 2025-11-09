import string


def checkPalindrome(given_word):
    clean_word = ""
    for char in given_word:
        if char not in string.punctuation:
            clean_word += char

    clean_word = clean_word.lower().replace(" ", "")
    reversed_word = clean_word[::-1]
    print(clean_word)
    print(reversed_word)

    if clean_word == reversed_word:
        return True
    else:
        return False

given_word =  "A man, a plan, a canal: Panama"

print(checkPalindrome(given_word))

