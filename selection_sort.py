#Converting String List into Int List
def string_to_int(array_string):
    array_int = []
    for x in array_string:
        array_int.append(int(x))
    return array_int

#Function for finding min element index in an array
def find_min(array,start, end):

    min_element_index = start
    for i in range(start+1, end + 1):
        if(array[min_element_index] > array[i]):
            min_element_index = i

    return min_element_index


#Recursive Function Selection Sort
def selection_sort_recursive(array, start, end):

    if (start != end):
        min_value_index = find_min(array,start,end)
        array[start],array[min_value_index] = array[min_value_index],array[start]
        selection_sort_recursive(array, start+1, end)


#Iterative Function Selection Sort
def selection_sort_iterative(array):
    for i in range(len(array)-1):
        min_index = find_min(array,i,len(array)-1)
        array[i],array[min_index] = array[min_index],array[i]



# Main program
def main():
    unsorted_array = input("Enter the unsorted array ").split(" ")
    unsorted_array = string_to_int(unsorted_array)
    # selection_sort_recursive(unsorted_array,0, len(unsorted_array)-1)
    selection_sort_iterative(unsorted_array)
    print(unsorted_array)
if (__name__ == "main"):
    # This block will only execute if this script is run directly
    main()
