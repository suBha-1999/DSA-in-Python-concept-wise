## as we have binary search with log2(n) complexity,
## we can also implement ternary search with log3(n) complexity
## as we know that lower the base, higher the value. so log3(n) < log2(n)

def TernarySerarch(arr, i, j, target):
    while(i<=j):
        mid_l = i +(j - i)//3
        mid_r = j - (j - i)//3
        if arr[mid_l] == target:
            return mid_l
        elif arr[mid_r] == target:
            return mid_r
        elif target < arr[mid_l]:
            return TernarySerarch(arr, i, mid_l-1, target)
        elif target > arr[mid_r]:
            return TernarySerarch(arr, mid_r+1, j, target)
        else:
            return TernarySerarch(arr, mid_l+1, mid_r-1, target)
    return -1

##driver code
arr = [20, 25, 47, 56, 59, 63, 65, 79, 82]
target = TernarySerarch(arr, 0, len(arr)-1, 63)
print("index of the target is: ", target)



## but in practical domain also in company there are Binary search is more Practical,
## because of the number of comparesion of ternary Search is more then Binary

############################ Thank you ##########################