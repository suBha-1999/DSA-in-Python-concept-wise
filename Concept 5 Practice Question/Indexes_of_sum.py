###   Given a sorted array [20, 40, 60, 80, 90, 120, 240]
##    you need to find the index of the elements, which provide sum A+B = 210,
###   we need to find index of (A,B)


##brute Force Algo   ------> pair search    -----> 0(n**2)
def Find_Pair(arr, target):
    n = len(arr)
    for i in range(n):        ##---------------  0(n)
        for j in range(i+1,n):   ##---------------0(n)
            if arr[i] + arr[j] == target:
                return i,j
    return -1


### we can reduce the complexity to 0(n*logn)
## Apply Binary Search
def find_pair_binary(arr, target):
    n = len(arr)
    for i in range(n):
        rem = target - arr[i]
    ## Now you can apply Binary Search
        l, r = i+1, n-1
        while(l <= r):
            mid = l + (r - l)//2
            if arr[mid] == rem:
                return i, mid
            elif arr[mid] < rem:
                l = mid + 1
            else:
                r = mid - 1
    return -1


## we can also reduce the complexity to 0(n) using
# ## -------------two Pointer approach-----------## #
def Find_Pair_TP(arr, target):
    n = len(arr)
    l, r = 0, n-1
    while(l < r):    ##------------------------ 0(n)
        if(arr[l] + arr[r] == target):
            return l,r
        elif arr[l] + arr[r] < target:
            l = l + 1
        else:
            r = r - 1
    return -1




## driver code
Arr = [20, 40, 60, 80, 90, 120, 240]
target = 210
result = Find_Pair(Arr, target)
print(result)
result1 = find_pair_binary(Arr, target)
print(result1)
result2 = Find_Pair_TP(Arr, target)
print(result2)