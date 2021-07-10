# creating an empty list
user_words_list = []

# number of elements as input
user_input = int(input("Enter the number of strings you want to compare and sort : "))

# iterating till the range of user choice and adding them to the list of words
for i in range(0, user_input):
    element = (input("Please enter the string you want in the list: "))
    user_words_list.append(element)  # adding the element to the list
    # Sorting a string
    print("Added to the list:", user_words_list)


def convert(unsorted_user_list):
    for i in range(len(unsorted_user_list)):
        for j in range(i + 1,len(unsorted_user_list)):
            if unsorted_user_list[i] > unsorted_user_list[j]:
                temp= unsorted_user_list[i]
                unsorted_user_list[i]=unsorted_user_list[j]
                unsorted_user_list[j] = temp
    return unsorted_user_list




print("\nRESULTS:")
print("\nThe sorted list in the order: ")
#call the function
print(convert(user_words_list))

#testcase
rand_list=['jbhd', 'zzd', 'alo', 'lpp', 'kd', '100','500','.009','hello',':)','!','16', '19', '13', '18', '15','Programming','INFO 5502','$$']
print(" \nBefore sorting:",rand_list)
print("After sorting:",convert(rand_list))

#testcase2
rand_list2=['100', '19', '23', '.09', '.000001']
print(" \nBefore sorting:",rand_list2)
print("After sorting:",convert(rand_list2))

#testcase3
rand_list3=['zz', 'nn', 'olk', 'jey', 'whatsup!']
print(" \nBefore sorting:",rand_list3)
print("After sorting:",convert(rand_list3))

#testcase3
rand_list3=['zz', 'nn', 'olk', 'jey', 'whatsup!']
print(" \nBefore sorting:",rand_list3)
print("After sorting:",convert(rand_list3))

#testcase5
rand_list5=['life', '!123', '$$money', 'Question', 'Great']
print(" \nBefore sorting:",rand_list5)
print("After sorting:",convert(rand_list5))




