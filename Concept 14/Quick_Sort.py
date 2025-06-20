## Function Declaration for partitionAlgo, main Algo for Quick Sort
def partitionAlgo(arr, p, q):
    
    ## Step 1: assume a Pivot element
    pivot = arr[p]  ## no need to take any variable, for remember purpose
    print(pivot)
    
    ## Initilise the index of i as start from 0 
    i = p
    
    ## Also initilize the Index of j from next index or i 
    for j in range(i+1, q+1):
        if arr[j] <= pivot: ## Always compare the j'th element with pivot/ arr[p]'th element
            i += 1          ## If true, First incress/ jump i'th value 1 step 
            arr[i], arr[j] = arr[j], arr[i] ## Then Swap the value between arr[i] and arr[j]
            
    ## Last you definatly need a swap between arr[i] and arr[p] **** NOT pivot ****
    ## Because if you swap between pivot and arr[i], it don't modify the original array, it only change pivot value
    arr[i], arr[p] = arr[p], arr[i]
    return i 
    
    
def quickSort(arr, i, j):
    if i < j:
        ## Like marge Sort you need to find a element for divide the array into 2 parts 
        m = partitionAlgo(arr, i, j)
        
        ## Recurrence will took part for left subarray
        quickSort(arr, i, m-1)
        
        ## Recurrence will took part for right Subarray
        quickSort(arr, m+1, j)
    return arr
    


# Driver code

arr = [50, 40, 70, 10, 30, 90, 45, 67, 79]
i, j = 0, len(arr)-1

res = quickSort(arr, i, j)
print(res)