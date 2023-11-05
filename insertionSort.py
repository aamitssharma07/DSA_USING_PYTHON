
#Converting String List into array List
def string_to_int(array_string):
    x = 0
    array_int = []
    for x in array_string:
        array_int.append(int (x))
    return array_int

def insertionSort(array_input):
    for x in range (0, len(array_input)-1):
        i = x
        key = array_input[i+1]
        while(i >= 0 and key < array_input[i] ):
          array_input[i+1] = array_input[i]
          i -= 1
        array_input[i+1] = key

array_input = input("Enter an array of integers: ").split(" ")
array_input = string_to_int(array_input)
insertionSort(array_input)
print(array_input)








