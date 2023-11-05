
#Function for converting string list into int string
def string_to_int(array_string):
        array_int = []
        for x in array_string:
            array_int.append(int(x))
        return array_int

#Function for searching in an array
def linear_array_search(search_element,array):
    for index, value in enumerate(array):
        if (search_element == value):
            return index

    return -1

# Function for searching in a Linked List
def linear_linklist_search(linked_list,search_element):



#Main Program
user_choice = input("You want to search in Array or LinkList? A/L ")
if(user_choice=="A"):
    input_array= input("Enter the array ").split(" ")
    input_array = string_to_int(input_array)
    search_element = int(input("Enter the element you want to search "))
    searched_element = linear_array_search(search_element, input_array)
elif(user_choice == "L"):

    search_element = int(input("Enter the element you want to search "))
    linked_list = deque();
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.appendleft(0)
    searched_element = linear_linklist_search(linked_list, search_element)
else:
    print("Enter either A or L")

if(searched_element >=0 ):
    print(f"Element {search_element} is present at index {searched_element}")
else:
    print(f"Element {search_element} is not present")



