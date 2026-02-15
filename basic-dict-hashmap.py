# d = {}
# d['a'] = 1
# d['b'] = 2
# print(d)
'''
class Demo(object):
    def countfreq(self, s):
        freq={}
        for ch in s :
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]=freq[ch]+1
        print(freq)


s = "ankitakn"
d = Demo()
d.countfreq(s)

#time and space both complexity -. O(n) 
'''


#count frequency of numbers 


'''
class Demo(object):
    def countfreq(self, arr):
        freq={}
        for ch in arr:
            if ch in freq:
                freq[ch]=freq[ch]+1
            else:
                freq[ch]=1
        return freq


arr = [1, 2, 2, 3, 1, 4, 2]
d = Demo()
print(d.countfreq(arr))
'''


#First Non-Repeating Character

'''class Demo(object):
    def nonrepeatchar(self, s):
        freq={}
        freq1={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]=freq[ch]+1
        #print(freq)
        for ch in s:
            if freq[ch]==1:
                return ch
        #return None
        


s = "aabbcdde"
d = Demo()
print(d.nonrepeatchar(s))'''

#check string anagram 

'''
class Demo(object):
    def stranagram(self,s1,s2):
        if len(s1) != len(s2):
            return False
        freq={}
        freq1={}
        for ch in s1:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]=freq[ch]+1
        print(freq)
        for ch in s2:
            if ch not in freq1:
                freq1[ch]=1
            else:
                freq1[ch]=freq1[ch]+1
        print(freq1)
        return freq==freq1
        # if freq==freq1:
        #     return True
        # else:
        #     return False
            

s1 = "listen"
s2 = "silten"
d = Demo()
print(d.stranagram(s1,s2))


#remove duplicate 
class Demo(object):
    def removeduplicate(self, s):
        freq={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]=freq[ch]+1
        print(freq)
        
        
s = "aabbcdde"      
d = Demo()
d.removeduplicate(s)
'''

'''#Count Frequency of Words

class Demo(object):
    def countfreqwords(self,s):
        freq={}
        s=s.split()
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        print(freq)

s = "apple banana apple orange banana apple"
d=Demo()
d.countfreqwords(s)
#time :O(n) and space O(k) -- k is unique words
'''

#Two Sum (sorted Array )
'''class Demo(object):
    def twosum(self,arr,target):
        left=0
        right=len(arr)-1
        sum=0
        while left<right:
            sum=arr[left]+arr[right]
            if sum==target:
                return arr[left],arr[right]
            elif sum>target:
                right-=1
            else:
                left+=1
        return False
        

arr = [2,7,11,15]
target = 9,
d=Demo()
print(d.twosum(arr,target))'''

#two sum - unsorted 



class Demo(object):
    def twosum(self, arr, target):
        seen = {}   # store numbers we have visited

        i = 0
        while i < len(arr):
            num = arr[i]
            diff = target - num

            if diff in seen:
                return diff, num

            seen[num] = True
            i += 1

        return None


arr = [11, 2, 15, 7]
target = 9
d = Demo()
print(d.twosum(arr, target))

#find all duplicate in array

class Demo(object):
    def findduplicate(self, arr):
        freq={}
        for ch in arr:
            if ch in freq:
                freq[ch]=freq[ch]+1
            else:
                freq[ch]=1
        for ch in freq:
            if freq[ch] !=1:
                print(ch)

arr = [1,2,3,2,4,5,1]
d = Demo()
print(d.findduplicate(arr))
