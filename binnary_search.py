#Function for converting string list into int string
def string_to_int(array_string):
        array_int = []
        for x in array_string:
            array_int.append(int(x))
        return array_int


#Recursive Function for Binnary search
def binnary_search(sorted_array, search_element, start, end, length):
    if(length > 0):
        mid = (end - start)//2
        if (sorted_array[mid]== search_element):
            return mid
        elif(sorted_array[mid] > search_element):
            binnary_search(sorted_array,search_element,start, mid -1,mid-start)
        else:
            binnary_search(sorted_array, search_element,  mid + 1,end,  end - mid)
    return -1

#Iterative Function for Binnary search
def binnary_search_iterative(unsorted_array,search_elem):

    length = len(unsorted_array)
    mid = (length-1)// 2
    while(length > 0):
        if(unsorted_array[mid]== search_elem):
            return  mid
        elif(unsorted_array[mid] >= search_elem):
            mid = (mid-1)//2
            length = mid +1
        else:
            mid = mid + (len(unsorted_array) - mid)//2
            length = len(unsorted_array)-mid
    return -1



# Main Program of Binnary Search
input_array= input("Enter the sorted array ").split(" ")

input_array = string_to_int(input_array)
search_element = int(input("Enter the element you want to search "))

# Function Call for recusrive Version Of Binnary Saerch
searched_element = binnary_search(input_array,search_element, 0, len(input_array)-1,len(input_array))
print("Recursive Binnary Search")
if(searched_element >=0 ):
    print(f"Element {search_element} is present at index {searched_element}")
else:
    print(f"Element {search_element} is not present")

#Function Call for Iterative Version Of Binnary Saerch
searched_element = binnary_search_iterative(input_array,search_element)
print("Iterative Binnary Search")
if(searched_element >=0 ):
    print(f"Element {search_element} is present at index {searched_element}")
else:
    print(f"Element {search_element} is not present")