class solution:

    def scoreofparentheses(self,str):
        stack=[0]
        for s in str:

            if s=="(":
                ab=stack.append(0)
            else:
                tmp=stack.pop()
        
                val=2*tmp if tmp > 0 else 1
                stack[-1]+=val

        return stack[-1]

s1=solution()
str="(()(()))"
ans=s1.scoreofparentheses(str)
print("Score of parentheses:",ans)                