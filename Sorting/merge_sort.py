""" Divide the unsorted list into  sublists, each containing  element.
Take adjacent pairs of two singleton lists and merge them to form a list of 2 elements.  will now convert into  lists of size 2.
Repeat the process till a single sorted list of obtained. """
def mergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        
        i = 0
        j = 0
        k = 0
        print(left_arr, right_arr, arr)
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
                
                

if __name__ == '__main__':
    arr = [2, 6, 5, 1, 7, 4, 3]     
    mergeSort(arr)
    print(arr)
