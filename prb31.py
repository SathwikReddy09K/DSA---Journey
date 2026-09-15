class solution:
    def lengthoflongest_substring(self,str):
        dict={}
        length=0
        prev_len=0
        for i in range(len(str)):
            comp=str[i]
            if comp in dict:
                dict.clear()
                prev_len=0
            dict[comp]=i
            prev_len+=1
            if prev_len>length:
                length=prev_len
        return length        

            
s1=solution()
str=input("Enter string:")
ans=s1.lengthoflongest_substring(str)  
print("Longest substring without repeating characters:",ans)        