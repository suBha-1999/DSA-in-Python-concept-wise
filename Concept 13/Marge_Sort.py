def margeProcedure(arr, i, mid, j):

    # calculate the size of subarray that is needed
    m = mid - i + 1
    n = j - mid

    # create array using size of 2 subarray
    leftSubarray = [0] * m
    rightSubarray = [0] * n

    # place the element place in array to subarray
    for x in range(m):
        leftSubarray[x] = arr[i + x]

    for y in range(n):
        rightSubarray[y] = arr[mid + 1 + y]

    # compare and compile
    p = 0
    q = 0
    k = i

    # jab tak ek ka v pointer last tak nehi jata p or q badhta rahega
    while p < m and q < n:

        if leftSubarray[p] <= rightSubarray[q]:
            arr[k] = leftSubarray[p]
            p += 1

        else:
            arr[k] = rightSubarray[q]
            q += 1
        k += 1
    # jab right subarray khatam ho geya par left abhi v baki hain
    while p < m:
        arr[k] = leftSubarray[p]
        p += 1
        k += 1

    # abar left subarray khatam hain but right baki hain
    while q < n:
        arr[k] = rightSubarray[q]
        q += 1
        k += 1

    return arr


def margeSort(arr, i, j):
    if i < j:
        mid = i + (j - i) // 2

        margeSort(arr, i, mid)
        margeSort(arr, mid + 1, j)

        margeProcedure(arr, i, mid, j)

    return arr


# driver unicode

arr = [50, 70, 65, 13, 80, 62, 98, 27]
i = 0
j = len(arr) - 1

result = margeSort(arr, i, j)
print(result)
