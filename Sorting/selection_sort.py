# The Selection sort algorithm is based on the idea of finding the minimum or 
# maximum element in an unsorted array and then putting 
# it in its correct position in a sorted array.
def selectionSort(arr):
    for i in range(len(arr)):
        minimum = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                index = j
        tmp = arr[i]
        arr[i] = minimum
        arr[index] = tmp
            
    print(arr)
            

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 5, 6, 7, -4]
    print("Given array is", end="\n")
    print(arr)
    selectionSort(arr)