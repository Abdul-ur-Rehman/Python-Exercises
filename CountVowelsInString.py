def countVowel(word):
    word_length = len(word)
    count = 0
    for i in range(word_length):
        word = word.lower()
        if word[i] == "a" or word[i] == "e" or  word[i] == "i" or word[i] == "o" or word[i] == "u":
            count += 1
    return count

# Simpler version

def simple_countVowel(word):
    word = word.lower()
    count = 0
    for char in word:
        if char in "aeiou":
            count += 1
    return count


word = "Abdul-ur-Rehman"
print(countVowel(word))
print(simple_countVowel(word))
