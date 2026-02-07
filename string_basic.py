'''
Reverse a String

Problem: Reverse the given string.

Input: "hello"
Output: "olleh"


class Demo(object):
    def revstring(self,s1):
        start=0
        end=len(s1)-1
        s1=list(s1)
        while start<=end:
            s1[start],s1[end]=s1[end],s1[start]
            start+=1
            end-=1
        return ''.join(s1)

d=Demo()
s1="hello"
print(d.revstring(s1))
'''


#Count Vowels and Consonants
'''
class Demo(object):
    def count1(self, s1):
        vowels_set = "aeiouAEIOU"
        vowel = 0
        con = 0

        for ch in s1:
            if ch.isalpha():  # only letters
                if ch in vowels_set:
                    vowel += 1
                else:
                    con += 1

        return vowel, con


d = Demo()
s1 = "programming"
print(d.count1(s1))
'''
#Check Palindrome

'''
class Demo(object):
    def pal(self, s1):
        start=0
        end=len(s1)-1
        while start<=end:
            if s1[start]!=s1[end]:
                return False
            start+=1
            end-=1
        return True
        #return False
            

d = Demo()
s1 = "nitin"
print(d.pal(s1))
'''

#Check if Two Strings are Anagrams
class Demo(object):
    def anagram(self, s1,s2):
        for n in s1:
            if n in s2:
                return True
            else:
                return False

d = Demo()
s1 = "silent"
s2 = "listen"
print(d.anagram(s1,s2))