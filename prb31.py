class solution:
    def longest_substring(self,str):
        n=len(str)
        vis=[False]*26
        left=0
        right=0
        res=0
        while right < len(str):
            while vis[ord(str[right])-ord("a")]==True:
                vis[ord(str[left])-ord("a")]=False
                left+=1

            vis[ord(str[right])-ord("a")]=True
            res=max(res,right-left+1)
            right+=1 

        return res      
        
s1=solution()
str=input("Enter string:")
ans=s1.longest_substring(str)  
print("Longest substring without repeating characters:",ans)        

