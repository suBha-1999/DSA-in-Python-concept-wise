## Method implementation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                #swap need to do
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


## Driver code
arr1 = [70, 20, 50, 60, 35, 47]
result_bs = bubble_sort(arr1)
print(result_bs)