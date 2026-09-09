class solution:

    def reversing_string(self,str):
        n=len(str)
        for i in range(int(n/2)):
            str[i],str[n-i-1]=str[n-i-1],str[i]
        return str

s1=solution()
str=input("Enter string:")

str=list(str)
print("Original string in list:",str)

ans=s1.reversing_string(str)      
print("After reversing string:",ans) 