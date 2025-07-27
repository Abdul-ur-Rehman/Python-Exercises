def countOccurances(sports, word):

    count = 0
    for i in sports:
        if i == word:
            count += 1

    return count


sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
word = "Football"

print("Sports: ", sports)
print("Word: ", word)
print("Total Occurances:", countOccurances(sports, word))