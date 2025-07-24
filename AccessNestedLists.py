#Actual Problem ==> Given a nested list, print the element '55'
#I am printing the list containing '55
nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]

for i in nested_list:
    for j in i:
        if j == 55:
            print(i)

