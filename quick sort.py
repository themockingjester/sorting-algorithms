# taken help from youtuber anuj bhaiya but implementd by own
arr = [10,7,8,9,1,8,5]
def quickSort(arr,l,h):
    if l<h:
        mid =h
        pivotIndex = partition(mid,l,h,arr)
        
        quickSort(arr,l,pivotIndex-1)
        quickSort(arr,pivotIndex+1,h)
def partition(pivotIndex,l,h,arr):
    
    i=l
    j = h
    while i<j:
        
        while arr[i]<=arr[pivotIndex]:
            
            i+=1
            if i>h:
                i=h
                break
                    
        while arr[j]>arr[pivotIndex]:
            
            j-=1
            if j<l:
                j=l
                break
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[pivotIndex],arr[j]=arr[j],arr[pivotIndex]
    return j
            
quickSort(arr,0,len(arr)-1)
print(str(arr)+" "+"ans")
