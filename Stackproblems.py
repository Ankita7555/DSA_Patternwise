# class StackDemo(object):
#     stack=[]
#     stack.append(10)
#     print(stack)
#     stack.append(20)
#     stack.pop()
#     print(stack[-1])
    
#In Python, stack is just a list.

#There is no special stack type.
#but we treat that as stack using append and pop opertaion
#reverse string using stack
'''
class StackDemo(object):
    def revstack(self, s):
        stack=[]
        s1=[] #empty list
        for ch in s:
            stack.append(ch)
        print(stack)
        while stack:
            #s1+=stack.pop() #+ take more time so use stack
            s1.append(stack.pop())
        return "".join(s1)

d = StackDemo()
s = "ankita"
print(d.revstack(s))
'''
'''
Method	Time Complexity
+= string method -	O(n²)
list + join method - O(n)
'''

#Remove Adjacent Duplicates (stack classic)

# class StackDemo(object):
#     def removedup(self, s):
#         stack=[]
#         for ch in s:
#             #stack.append(ch)
#             if stack and stack[-1] == ch:
#                 stack.pop()
#             else:
#                  stack.append(ch)
#         return "".join(stack)

# d = StackDemo()
# s = "aabbaca"
# #op:ca Time: O(n) Space: O(n)
# print(d.removedup(s))
#if stack means it is checking if stack is not empty 
#for first time condition is getting false so it is appending from 2 insert onwards that consition is checking


# Valid Parentheses (Simple Version)
'''class StackDemo(object):
    def validpar(self, s):
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(ch)
            else:
                if len(stack)<=0:
                    return False
                stack.pop()
        if len(stack)<=0:
            return True
        else:
            return False
d = StackDemo()
print(d.validpar("(()())"))  # True
print(d.validpar("(()"))     # False
print(d.validpar("(()))"))   # False
print(d.validpar("(())"))    # True

# Time: O(n) and Space: O(n)


class StackDemo(object):
    def validpar(self, s):
        stack = []
        for ch in s:
            if ch=="(" or ch=="{" or ch=="[":
                stack.append(ch)
            else:
                if len(stack)<=0:
                    return False
                
                top=stack.pop()
                
                if ch=="}" and top!="{":
                    return False
                elif ch==")" and top!="(":
                    return False
                elif ch=="]" and top!="[":
                    return False
        if len(stack)==0:
            return True
        else:
            return  False       


d = StackDemo()
print(d.validpar("{[]}"))   # True
print(d.validpar("(]"))     # False
print(d.validpar("([)]"))   # False
print(d.validpar("{([])}")) 


#Time: O(n) and Space: O(n)
'''

#check palindrome using stack
'''
class StackDemo(object):
    def palcheck(self, s):
        stack=[]
        s2=""
        for ch in s:
            stack.append(ch)
        while len(stack)>0:
            s2+=stack.pop()
        return s==s2

d = StackDemo()
s = "madam"
print(d.palcheck(s))
#time n space :O(n) two pointer is more optmized cause need space as O(n) and space O(1) 

'''


#sum using stack [1,2,3,1] o/p:7

class StackDemo(object):
    def sumstack(self, arr):
        stack = []
        total = 0
        # push all elements
        for num in arr:
            stack.append(num)
        # pop and add
        while len(stack) > 0:
            total += stack.pop()
        return total

d = StackDemo()
arr = [1, 2, 3, 1]
print(d.sumstack(arr))  # 7










