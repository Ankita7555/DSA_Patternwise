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
'''


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



#two number addition
'''
class Demo(object):
    def twosum(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:
            s = arr[left] + arr[right]

            if s == target:
                print(arr[left], arr[right])
                return True
            elif s < target:
                left += 1
            else:
                right -= 1

        return False


arr = [0,1,2,2,3,4,6,9,8]
target = 7
d = Demo()
d.twosum(arr, target)



# 3 number continuos sum

class Demo(object):
    def sumofthree(self,arr,k):
        windonw_sum=sum(arr[0:k])
        max_sum=windonw_sum
        for i in range(k,len(arr)):
            windonw_sum+=arr[i]
            windonw_sum-=arr[i-k]
            max_sum=max(max_sum,windonw_sum)
            
        return max_sum

arr=[4, 2, 1, 7, 8, 1, 2, 8]
k=3
d=Demo()
print(d.sumofthree(arr,k))

#time O(N) and space O(1)




class Demo(object):
    def sumofthree(self,arr,k):
        windonw_sum=sum(arr[0:k])
        max=windonw_sum/k
        print(max)
        #max_sum=windonw_sum
        for i in range(k,len(arr)):
            windonw_sum+=arr[i]
            windonw_sum-=arr[i-k]
            #max_sum=windonw_sum
            print(windonw_sum/k)
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
d=Demo()
d.sumofthree(arr,k)

#way 2 using new empty array - store values

class Demo(object):
    def averageOfSubarrays(self, arr, k):
        window_sum = sum(arr[:k])
        result = []

        result.append(window_sum / k)

        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]
            result.append(window_sum / k)

        return result


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
d = Demo()
print(d.averageOfSubarrays(arr, k))




'''

