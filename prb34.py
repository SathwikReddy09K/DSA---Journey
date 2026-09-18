class solution:
    def check_permutation(self,str1,str2):
        str1=str1[::-1]             # Reversing string,it is one permutation
        k=len(str1)
        for i in range (len(str2)-k):
            if str2[i:k+i]==str1:
                return True
        return False    
        

s1=solution()
str1=input("Enter sub string:")
str2=input("Enter string:")
ans=s1.check_permutation(str1,str2)
print(f"permutation of {str1} in {str2} string is ",ans)