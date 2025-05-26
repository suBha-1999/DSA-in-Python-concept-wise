##   If an unsorted array is given to you and after some valid natural number from starting,
##   index value will 'inf'.    You need to find the index of first 'inf'.

## as the array is unsorted we can use Linear sort Algo

import math

def FindIndex(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == math.inf: ## math.inf == float('inf')
            return i

##Driver code
arr = [-23, 40, 55, 1, 4, 27, 56, -89, math.inf, math.inf, math.inf, math.inf]
result = FindIndex(arr)
print(result)
## But here the time complexity is 0(n)








## if we want to reduce the time complexity, in my opinion Modified binary search will be an option

def FindInf_update(arr, i, j):
    while(i <= j):
        mid = i + (j-i)//2
        if isinstance(arr[mid], int):
            i = mid + 1
        if arr[mid] == math.inf :
            j = mid - 1
    return mid


## driver code
arr1 = [-23, 40, 55, 1, 4, 27, 56, -89, math.inf, math.inf, math.inf, math.inf]
result_new = FindInf_update(arr1, 0, len(arr1))
print(result_new)


