class solution:
    def check_anagram(self,str1,str2):
        n1=len(str1)
        n2=len(str2)
        str1="".join(sorted(str1))
        str2="".join(sorted(str2))
        i=0
        while i < n1  or i < n2:
            if [ord(str1[i])] != [ord(str2[i])] :
                return False
            i+=1
        return True

s1=solution()
str1=input("Enter string 1:")
str2=input("Enter string 2:")
ans=s1.check_anagram(str1,str2)
print("The two strings are anagrams of each other:",ans)    
            