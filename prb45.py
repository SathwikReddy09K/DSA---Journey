class solution:
    def merge_arrays(self,num1,num2):
        n1=len(num1)
        n2=len(num2)
        j=i=0
        merge=[]
        while(i < n1 and j < n2):
            if num1[i] < num2[j]:     
                merge.append(num1[i])
                i+=1
            else:
                merge.append(num2[j])
                j+=1

        merge.extend(num1[i:])
        merge.extend(num2[j:])

        return merge


    def medianofmergearray(self,arr):
        n=len(arr)
        mid_term=n//2
        if n%2 == 0:
            median=(arr[mid_term-1] + arr[mid_term])/2

        else:
            median=(arr[mid_term])

        return median


s1=solution()
num1=list(map(int,input("Enter array1 values in sorted order:").split()))   #Example:num1=[1,5,7],num2=[3,6]
num2=list(map(int,input("Enter array2 values in sorted order:").split()))
arr=s1.merge_arrays(num1,num2)
print(arr)
ans=s1.medianofmergearray(arr)
print(ans)           