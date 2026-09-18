class solution:
    def longest_ksubstring(self,str,k):
        dict={}
        length=0
        prv_length=0
        j=1
        for i in range(len(str)):
            comp=str[i]
            if comp in dict :
                if dict[comp] >k:
                    dict.clear()
                    prv_length=0
                else:
                    prv_length+=1    
            else: 
                dict[comp]=j
                j+=1
                prv_length+=1
            if prv_length > length:
                length=prv_length
        return length        
        
                               
s1=solution()
str=input("Enter string:")
k=int(input("Enter size of k: "))
ans=s1.longest_ksubstring(str,k)  
print("Longest substring without repeating characters:",ans)        