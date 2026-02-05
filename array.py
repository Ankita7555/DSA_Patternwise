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
    
d=Demo()
num=[1,4,3,2,6,8,9]
print(d.secondlarge(num))
