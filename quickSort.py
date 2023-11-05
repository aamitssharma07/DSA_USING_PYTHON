#Function for converting string list into int string
def string_to_int(array_string):
        array_int = []
        for x in array_string:
            array_int.append(int(x))
        return array_int


def swap(x,y):
    temp = x
    x = y
    y = temp



#Heart of the Quick sort Algo is Partitioning function
def partitioning(input_array, start, end):
    i = start-1
    j = start
    pivot =  end
    #Scans the whole array
    for j in range(start,end):
        #Swap value of i and j index if ith <= jth element
        if(input_array[j] <= input_array[pivot]):
            i += 1
            input_array[i],input_array[j] = input_array[j], input_array[i]

        else:
            j += 1
    input_array[i+1], input_array[pivot] = input_array[pivot], input_array[i+1]
    return i+1



#QuickSort Function

def quick_sort(input_array, start, end):
    if(start < end):
        pivot = partitioning(input_array,start, end)
        quick_sort(input_array,start,pivot-1)
        quick_sort(input_array,pivot+1,end)


#Main program of Quick Sort
unsorted_array = input("Enter the unsorted array ").split(" ")
unsorted_array = string_to_int(unsorted_array)

quick_sort(unsorted_array,0,len(unsorted_array)-1)
print(unsorted_array)
