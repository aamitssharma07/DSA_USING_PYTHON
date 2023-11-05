#Converting String List into Int List
def string_to_int(array_string):
    array_int = []
    for x in array_string:
        array_int.append(int(x))
    return array_int

# function for merging two sorted arrays
def merging(unsorted_array,start,separation,end):
    array1 = []
    array2 = []
    for x in range(start,separation+1):

        array1.append(unsorted_array[x])
    for y in range(separation+1,end+1):

        array2.append(unsorted_array[y])
    i=j = 0
    for k in range(start, end+1):
        if (i >= len(array1)):
            for j in range(j, len(array2)):
                unsorted_array[k] = array2[j]
        elif (j >= len(array2)):
            for i in range (i, len(array1)):
                unsorted_array[k] = array1[i]
        elif (array1[i] <= array2[j] and i < len(array1)):
            unsorted_array[k] = array1[i]
            i += 1
        # else (array2[j]  <  array1[i] and j < len(array2)):
        else:
            unsorted_array[k] = array2[j]
            j += 1



# function for merge sort

def mergeSort(unsortedArray, start, end):
    if start < end:
        mid =(start + end)//2
        mergeSort(unsortedArray,start, mid )
        mergeSort(unsortedArray,mid + 1, end)
        merging(unsortedArray, start, mid, end)





#Main program
unsortedArray = input("Enter the unsorted array ").split(" ")
unsortedArray = string_to_int(unsortedArray)
mergeSort(unsortedArray,0,len(unsortedArray)-1)
print(unsortedArray)











