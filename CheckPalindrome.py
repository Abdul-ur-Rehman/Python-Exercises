def checkPalindrome(string):

    string = string.lower()
    length = len(string)
    palindrome = ""
    while length > 0:
        palindrome += string[length-1]
        length -= 1

    if string == palindrome:
        return True
    else:
        return False

string= "Rotator"
print(checkPalindrome(string))