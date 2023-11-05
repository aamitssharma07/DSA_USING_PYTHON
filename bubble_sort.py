#Function for converting string list into int string
def string_to_int(array_string):
        array_int = []
        for x in array_string:
            array_int.append(int(x))
        return array_int

#Recusrsive Program for Bubble Sort
def bubble_sort_recurssive(unsorted,start,end):
    if(end != start):
        for i in range(start,end):
            j = i+1
            if(unsorted_array[i]>unsorted_array[j]):
                unsorted_array[i], unsorted_array[j] = unsorted_array[j], unsorted_array[i]
        bubble_sort(unsorted_array,start,end-1)

#Iterative Program for Bubble Sort Iterative
def bubble_sort_iterative(unsorted_array):
    length = len(unsorted_array)
    while(length != 1):
        for i in range(0,length-1):
            j = i + 1
            if(unsorted_array[i]>unsorted_array[j]):
                unsorted_array[i], unsorted_array[j] = unsorted_array[j],unsorted_array[i]
        length = length-1



#Main program
unsorted_array = input("Enter the unsorted array ").split(" ")
unsorted_array = string_to_int(unsorted_array)
# bubble_sort_recurssive(unsorted_array,0,len(unsorted_array)-1)
bubble_sort_iterative(unsorted_array)
print(unsorted_array)