def capitalizeFirstLetter(sentence):
    sen = sentence.split()
    length = len(sen)
    for i in range(length):
        capitalized_words = sen[i].capitalize()
        print("".join(capitalized_words), end=" ")



sentence = "pynative.com is for python lovers."

capitalizeFirstLetter(sentence)