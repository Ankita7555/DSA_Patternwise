# check palindrome or not - using two pointer 
# time : O(n) and space : O(1)

'''
class Demo(object):
    def pal(self,arr):
        left=0
        right=len(arr)-1
        while left<right:
            if(arr[left]!=arr[right]):
                return False
            left+=1
            right-=1
        return True
            
        
d=Demo()
arr='civic'
print(d.pal(arr))
'''

'''
# Reverse array using two pointer

class Demo(object):
    def revarray(self,arr):
        left=0
        right=len(arr)-1
        arr=list(arr)
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
            
        
d=Demo()
arr1=[1,2,3,4]
arr="ankita"
print(d.revarray(arr))

#time and space = O(n)  -- because we are converting string to array
'''

# two number sum input = array and target value

'''
class Demo(object):
    def twosum(self,arr,target):
        left=0
        right=len(arr)-1
        arr.sort() 
        while left<right:
            sum=arr[left]+arr[right]
            if target==sum:
                return arr[left] , arr[right]
            elif sum<target:
                left+=1
            else:
                right-=1
          
        return False
            
        
d=Demo()
arr=[3,1,2,4,6]
target=5
print(d.twosum(arr,target))

'''


# Time : O(n log n) (sort:O(n log n )) , Space :O(1). -- time complexity can be minimize using hashing

#rule:both num1 and num2 are sorted in asc order 9non desc)
# Leetcode - 88 88. Merge Sorted Array (two pointer)


'''
class Demo(object):
    def mergetwo(self,num1,num2,m,n):
        i=m-1
        j=n-1
        k=m+n-1
        while(i>=0 and j>=0):
            if(num1[i]>num2[j]):
                num1[k]=num1[i]
                i-=1
            else:
                num1[k]=num2[j]
                j-=1
            k-=1
        while(j>=0):
            num1[k]=num2[j]
            j-=1
            k-=1
        return num1   
      

num1=[-1,2,6,0,0]
num2=[2,5]
m=3
n=2
d=Demo()
print(d.mergetwo(num1,num2,m,n))

#space O(1) and time : O(m+n)




#move zeros to end 


class Demo(object):
    def movezeros(self,arr):
        left=0
        right=0
        for right in range(len(arr)):
            if (arr[right]!=0):
                 arr[left],arr[right]=arr[right],arr[left]
                 left+=1
        return arr        
d=Demo()
arr=[0,1,0,3,12]
print(d.movezeros(arr))
'''








#Remove Duplicates from Sorted Array

class Demo(object):
    def removedup(self, arr):


        left = 0  # slow pointer

        for right in range(1, len(arr)):  # fast pointer
            if arr[right] != arr[left]:
                left += 1
                arr[left] = arr[right]

        return arr[:left + 1]


d = Demo()
arr = [1, 1, 1,2, 3, 3,4]
print(d.removedup(arr))












