class solution:
    def three_sum(self,arr):
        pairs=[]
        dict={}
        for j in range(0,len(arr)):
            for k in range(j+1,len(arr)):

                # arr[i]+arr[j]+arr[k]=0
                # arr[i]=-(arr[j]+arr[k])
                val= -1*(arr[j]+arr[k])

                if val in dict:
                    pairs.append([dict[val],j,k])

            if arr[j]  not in dict:
                dict[arr[j]]=j
            
        return pairs
                


                

s1=solution()
arr=list(map(int,input("Enter array:").split()))
ans=s1.three_sum(arr)
print("Sum of triplets is equal to zero are",ans)