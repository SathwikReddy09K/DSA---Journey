def longestcommonprefix(arr):
    minlen=len(arr[0])
    for s in arr:
        minlen=min(minlen,len(s))
    res=""    
    for i in range (minlen): 
        if arr[0][i]==arr[1][i]==arr[2][i] :
           res=res+arr[0][i]
    return res       


arr=["apple","ape","april"]
ans=longestcommonprefix(arr)
print(f"longest common prefix of {arr} :",ans) 