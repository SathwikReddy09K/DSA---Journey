class solution:
    def check_permutation(self,s1,s2):
        n1=len(s1)
        n2=len(s2)
        c1=[0]*26
        c2=[0]*26
        for i in range(n1):
            c1[ord(s1[i])-ord('a')]+=1
            c2[ord(s2[i])-ord('a')]+=1

        if c1==c2:
            return True
        for i in range(n1,n2):
            c2[ord(s2[i])-ord('a')]+=1
            c2[ord(s2[i-n1])-ord('a')]-=1

            if c1==c2:
                return True
            
        return False    

s1=solution()
str1=input("Enter sub string:")
str2=input("Enter string:")
ans=s1.check_permutation(str1,str2)
print(f"permutation of {str1} in {str2} string is ",ans)