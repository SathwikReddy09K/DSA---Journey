class solution:
    def index_of_firstoccur_str(self,str1,str2):
        k=len(str2)
        str2=str2[:k]
        i=0
        while (i<len(str1)):
            if str1[i:k+i]==str2 :
                return i
            i=i+1
        return -1


s1=solution()
str1=input("Enter string(str1):")
str2=input("Enter string(str2):")
ans=s1.index_of_firstoccur_str(str1,str2)
print(ans)