def colour_sort(arr):

    n=len(arr)
    mid=int(n/2)
    end=n-1              
    start=0

    while start< len(arr)/2:

        if arr[start]==2:
            arr[start],arr[end]=arr[end],arr[start]
            end-=1

        if arr[start]==1:
            arr[start],arr[mid]=arr[mid],arr[start]

        start+=1    
    
    return arr

#input should be in the form of 0,1,2
arr=list(map(int,input("Enter array:").split()))       
 
ans=colour_sort(arr)
print("Final answer after sorting in order of 0,1,2:",ans)        
    