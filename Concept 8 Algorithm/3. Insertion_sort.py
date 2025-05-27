## Method implementation

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

## function definetion
arr = [75, 90, 95, 100, 85, 80]
result_val = insertion_sort(arr)
print(result_val)

