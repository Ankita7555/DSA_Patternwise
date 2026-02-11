#find larget number
'''
Docstring for array
Input:
[3, 7, 2, 9, 5]
Output:
9
'''
'''
class Demo(object):
    def findmax(self,num):
        max=num[0]
        for i in range(len(num)):
            if num[i]>max:
                max=num[i]
        return max
        
d=Demo()
num=[40,1,2,3,6,4,21,3,22]
print(d.findmax(num))


class Demo(object):
    def findmax(self,num):
        max=num[0]
        for val in num:
            if val>max:
                max=val
        return max
        
d=Demo()
num=[41,1,2,3,6,4,21,3,22]
print(d.findmax(num))

Time: O(n) ✅
Space: O(1) ✅
'''
'''
class Demo(object):
    def findmax(self,num):
        max=num[0]
        min=max
        for n in num:
            if n>max:
                max=n
            elif n<min:
                min=n
        return max,min
        
d=Demo()
num=[51,0,20,40,1,2,3,6,4,21,3,22,0,50]
print(d.findmax(num))
'''

#find sum of even numbers


class Demo(object):
    def findsumeven(self,num):
        sum=0
        for n in num:
            if n%2 == 0:
                sum+=n
        return sum

d=Demo()
num=[1,2,3,4,5,6,2]
print(d.findsumeven(num))


'''Given an array of numbers, find the second largest number.

Example

Input:
[1, 5, 3, 9, 7]
Output:
7
'''
'''
class Demo(object):
    def secondlarge(self,num):
        first=num[0]
        second=0
        for n in num:
            if n>first:
                second=first
                first=n
            elif n>second & n!=first:
                second=n
        return second
    
d=Demo()
num=[1,4,3,2,6,8,9]
print(d.secondlarge(num))

'''

#Given an array of numbers, find the third largest number.

class Demo(object):
    def secondlarge(self,num):
        first=num[0]
        second=0
        third=0
        for n in num:
            if n>first:
                third=second
                second=first
                first=n
            elif n>second and n!=first:
                third=second
                second=n
            elif n>third and n!=first and n!= second:
                third=n
        return third



#practise

# Template

'''window_sum = sum of first k elements
max_answer = window_sum

for i from k to end:
    window_sum += arr[i]        # add new element
    window_sum -= arr[i - k]    # remove old element
    update answer

return answer

'''

#max sum array
'''
class Demo(object):
    def maxSumSubarray(self, arr, k):
        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum += arr[i]      # add new element
            window_sum -= arr[i - k]  # remove old element
            max_sum = max(max_sum, window_sum)
            start = i - k + 1 
        return max_sum


d = Demo()
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(d.maxSumSubarray(arr, k))

class Demo(object):
    def maxSumSubarray(self, arr, k):
        window_sum = sum(arr[:k])
        max_sum = window_sum
        start = 0   # start index of max window

        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]

            if window_sum > max_sum:
                max_sum = window_sum
                start = i - k + 1   # window start index

        return max_sum, arr[start:start + k]


d = Demo()
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(d.maxSumSubarray(arr, k))

'''


#1 to 100
'''class Demo(object):
    def printstar(self):
        n=10
        for i in range(0,n):
            sp=" "*(n-i-1)
            sr="*"*(2*i+1)
            print(sp+sr)           

d=Demo()
d.printstar()
'''



#find max and min in array



'''class Demo(object):

    def printstar(self,arr):
        min=arr[0]
        max=arr[0]
        for i in range(0,len(arr)):
            if arr[i]>max:
                min=max
                max=arr[i]
            elif arr[i]<min and arr[i]!=max:
                min=arr[i]
            
            print(max,min)
                
                
arr=[0,5,10,300,51,772,51,2,5,5651]
d=Demo()
d.printstar(arr)
'''

'''
class Demo(object):

    def printstar(self,arr):
        min=arr[0]
        max=arr[0]
        for i in range(0,len(arr)):
            if arr[i]<min:
               min=arr[i]
            if arr[i]>max:
                max=arr[i]
        print(min,max)
                              
arr=[0,10,300,51,74472,51,2,5,1,565100,0,1]
d=Demo()
d.printstar(arr)
'''

'''class Demo(object):

    def printstar(self,arr):
        sum=0
        for i in range(len(arr)-1,-1,-1):
                sum+=arr[i]
        print(sum)
                              
arr=[5,10,20,30,40]
d=Demo()
d.printstar(arr)
'''


#second largest array


'''class Demo(object):

    def secondlarge(self,arr):
        secondmax=arr[0] 
        max=arr[0]
        for i in range(len(arr)):
            if arr[i]>max:
                secondmax=max
                max=arr[i]
            elif arr[i]>secondmax and arr[i]!=max: 
                secondmax=arr[i]
       
        print(max,secondmax) 
                              
arr=[5,13458880,20,3645680,5,40,26851,2]
d=Demo()
d.secondlarge(arr)
'''

'''

class Demo(object):

    def secondlarge(self,arr):
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        print(freq)
            
            
                              
arr=[5,2,3,5,1,5,2]
d=Demo()
d.secondlarge(arr)

'''

'''
class Demo(object):
    def movezero(self,arr):
        left=0
        for right in range(len(arr)):
            if arr[right]!=0:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
        return arr
                                       
arr=[0,5,0,0,0,2,0,5,0,5,2,0,0]
d=Demo()
print(d.movezero(arr))
'''
'''
class Demo(object):
    def revstr(self,arr):
        left=0
        right=len(arr)-1
        arr=list(arr)
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            right-=1
            left+=1
        return "".join(arr)
                                       
arr="ankita"
d=Demo()
print(d.revstr(arr))

'''




















d=Demo()
num=[1,4,3,2,6,8,9]
print(d.secondlarge(num))
