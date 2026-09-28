class solution:
    def longest_ksubstring(self,str,k):
        n=len(str)
        vis=[0]*26
        left=0
        right=0
        res=0
        count=0

        while right < len(str):
            if vis[ord(str[right])-ord("a")]==0:
                count+=1

            vis[ord(str[right])-ord("a")]+=1
            
            while count>k:
                vis[ord(str[left])-ord("a")]-=1

                if vis[ord(str[left])-ord("a")]==0:
                    count-=1
                    
                left+=1

            res=max(res,right-left+1)
            right+=1 

        return res
        
                               
s1=solution()
str=input("Enter string:")
k=int(input("Enter size of k: "))
ans=s1.longest_ksubstring(str,k)  
print(f"Longest substring  {k} unique :",ans)        