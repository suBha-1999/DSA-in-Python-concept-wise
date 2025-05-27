## Method implementation

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_elm = i
        for j in range(i+1, n):
            if(arr[j] < arr[min_elm]):
                min_elm = j
                print(min_elm)  # Print updated min_elm
        arr[i], arr[min_elm] = arr[min_elm], arr[i]
    return arr


# function defination
arr = [5, 20, 50, 30, 90, 70, 15]
result = selection_sort(arr)
print(result)
