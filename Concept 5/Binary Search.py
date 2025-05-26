## as Linear search time complexity is 0(n), binary search came into concept to reduce complexity
##***********BINARY SEARCH ALWAYS APPLICABLE OVER A SORTED ARRAY(ASCENDING OR DESCENDING ORDER)*********##
## as name consists binary means 2 part is there
## in this algo every step it decrees its search space into half
## n-> n/2-> n/4 .......

def BinarySearch(arr, l, r, target):
    while(l <= r):
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1
            BinarySearch(arr, l, r, target)
        else:
            r = mid - 1
            BinarySearch(arr, l, r, target)
    return -1


## Driver code

arr = [20, 30, 40, 50, 60, 70, 80, 90]
target = BinarySearch(arr, 0, len(arr)-1, 80)
print(target)

## as the array length always getting half, so we can say that
## Time complexity = 0(log2(n))---->where n belongs to => length of arr