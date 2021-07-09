# creating an empty list
user_words_list = []

# number of elements as input
user_input = int(input("Enter the number of strings : "))

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
print(convert(user_words_list))
print(sorted([999,100]))



