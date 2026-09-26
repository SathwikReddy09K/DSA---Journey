class solution:
    def frequency_counter(self,arr):
        dict={}
        for x in arr:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1

        return dict   

s1=solution() 
arr=list(map(int,input("Enter values:").split()))
ans=s1.frequency_counter(arr)
print("Frequency counter:",ans)