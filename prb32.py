class solution:
    def search(self,str1,str2):
        len2=len(str2)
        str2=''.join(sorted(str2))
        list=[]
        for i in range(len(str1)-len2+1):
            sub_str1=str1[i:i+len2]
            sub_str1=''.join(sorted(sub_str1))
            if sub_str1==str2:
                list.append(i)
        return list        

s1=solution()
str1=input("Enter string:")
str2=input("Enter sub string:")
result=s1.search(str1,str2)
print(f"Searching Angram substring in {str1}  are:",result)
