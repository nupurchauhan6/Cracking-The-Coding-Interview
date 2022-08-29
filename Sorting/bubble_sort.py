def bubbleSort(arr):
    for i in range(len(arr)):
        # len(arr) - i - 1, this is done because we know after every iteration the largest element will be
        # at the end of the arr so no need of comparison here
        for j in range(0 , len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    print(arr)
            

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 5, 6, 7, -4]
    print("Given array is", end="\n")
    print(arr)
    bubbleSort(arr)