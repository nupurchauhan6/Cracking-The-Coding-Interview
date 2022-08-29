# It iterates the input elements by growing the sorted array at each iteration. 
# It compares the current element with the largest value in the sorted array. 
# If the current element is greater, then it leaves the element in its place and 
# moves on to the next element else it finds its correct position in the sorted array 
# and moves it to that position. This is done by shifting all the elements, which are larger than the current element, in the sorted array to one position ahead
def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j != 0:
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
            j = j - 1   
    print(arr)      
            

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 5, 6, 7, -4]
    print("Given array is", end="\n")
    print(arr)
    insertionSort(arr)
