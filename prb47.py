def sotingarrayby_zeroes_ones_twos(arr):
    n=len(arr)
    low=mid=0
    high=n-1
    while mid <=high :
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1         

    return arr

#input should be in the form of 0,1,2
arr=list(map(int,input("Enter array:").split()))       
 
ans=sotingarrayby_zeroes_ones_twos(arr)
print("Final answer after sorting in order of 0,1,2:",ans)        
    