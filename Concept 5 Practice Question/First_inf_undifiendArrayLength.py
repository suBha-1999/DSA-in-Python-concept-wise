##if interviewer asked solve this question if not provide array length
##      Need to apply Exponential Search

import math
from First_inf import FindInf_update

def Exponential_search(Arr):
    if Arr[0] == math.inf:
        return 0
    i = 1
    while (Arr[i] != math.inf):
        i *= 2
    l,r = i//2 , i
    return FindInf_update(Arr, l, r)



arr = [-23, 40, 55, 1, 4, 27, 56, -89, math.inf, math.inf, math.inf, math.inf]
result = Exponential_search(arr)
print(result)

## Find the time complexity of this code...?