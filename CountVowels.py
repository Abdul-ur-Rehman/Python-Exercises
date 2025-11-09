
def countingVowels(given_String):
    count = 0
    for i in given_String:
        if i in "AEIOUaeiou":
            count += 1
    return count

given_String = "Abdul-ur-Rehman"

print(countingVowels(given_String))