from unittest.mock import sentinel


def occuranceOfSubstringInString(sentence, word):

    print("Original Sentence: ", sentence)
    count = 0

    for i in range(len(sentence)):
        if sentence[i: i+len(word)] == "Emma":
            count += 1

    return count

sentence = "Emma is good developer. Emma is a writer"
word = "Emma"
count = occuranceOfSubstringInString(sentence, word)
print(f"Emma appeared {count} times.")