## if you have an unsorted array and you need to find an element present in the array or not
##You need to apply Searching concept with Linear search algo

def LinearSearch(arr, target):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            return i
    return -1

## Driver Code
arr = [20, 45, 27, 47, 55, 67, 75, 88]
result = LinearSearch(arr, 55)
print(result)

## here for the best case time complexity will  be 0(1), for element present in 1st index
## and  for the worst case time complexity will be 0(n), for element present in last index=> arr[n-1]

## so avg complexity will be = 1/2 * best case + 1/2 * worst case
##                           = 1/2 * 0(1) + 1/2 * 0(n) ==============> 0(n)