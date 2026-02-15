'''FIFO — First In First Out

| Operation | Meaning           |
| --------- | ----------------- |
| Enqueue   | Add to back       |
| Dequeue   | Remove from front |
| Peek      | See front element |
| isEmpty   | Check if empty    |

'''
'''
class QDemo(object):
    def basics(self):
        queue = []
        queue.append(10)
        queue.append(20)
        queue.append(30)
        queue.append(40)
        queue.append(50)
        queue.pop(0)
        # it is slow cause need to go till that index O(n) time complexity so other approach : collection
        return queue

d=QDemo()
#print(d.basics())
'''

'''
| Method | Enqueue | Dequeue |
| ------ | ------- | ------- |
| List   | O(1)    | O(n) ❌  |
| deque  | O(1)    | O(1) ✅  |
dequeu() --> create double ended queue

'''

# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# queue.append(4)
# queue.popleft()
# queue.extend([5,6])
# #add multiple element to right
# queue.appendleft(7)
# print(queue)


'''Reverse First K Elements of Queue
queue = [1,2,3,4,5]
k = 3
[3,2,1,4,5]


from collections import deque
class Demo:
    def rev(self,queue):
        for i in range(k,0):
            queue.pop(i)
            print(queue)
        return queue   
     
d=Demo()
queue = [1,2,3,4,5]
k = 3
print(d.rev(queue))



from collections import deque

class QueueDemo(object):
    def reverseFirstK(self, queue, k):
        if k>len(queue):
            return False
        stack=[]
        for i in range(k):
            stack.append(queue.popleft())
        while len(stack)>0:
            queue.append(stack.pop()) 
        remaining = len(queue) - k

        for i in range(remaining):
            queue.append(queue.popleft())
            print(queue)

        return queue

# Example
queue = deque([1,2,3,4,5])
k = 3
d = QueueDemo()
print(d.reverseFirstK(queue, k))

'''
'''
The Core Logic
The Starting Point: We start with "1".

The Rule: For every number we take out of the queue, we generate two new ones:

The current number + "0"

The current number + "1"

The Queue (FIFO): Because a queue is "First-In, First-Out," it ensures we process all 1-digit numbers, then all 2-digit numbers, then 3-digit, and so on.
'''

# from collections import deque

# class QueueDemo(object):
#     def generateBinary(self, n):
#         queue = deque()
#         queue.append("1")

#         for i in range(n):
#             current=queue.popleft()
#             print(current)
#             queue.append(current+"0")
#             #print(queue)
#             queue.append(current+"1")
#             #print(queue)
#         print(queue)


# d = QueueDemo()
# d.generateBinary(5)

# from collections import deque
# class RecentCounter(object):
#     def __init__(self):
#         self.queue = deque()
#     def ping(self, t):
#         self.queue.append(t)
#         while self.queue[0] < t - 3000:
#             self.queue.popleft()
#         return len(self.queue)


# recentCounter=RecentCounter()
# recentCounter.ping(1);     
# recentCounter.ping(100);   
# recentCounter.ping(3001); 
# recentCounter.ping(3002); 


# class Solution(object):
#     def timeRequiredToBuy(self, tickets, k):
#         time = 0

#         for i in range(len(tickets)):
#             if i <= k:
#                 time += min(tickets[i], tickets[k])
#             else:
#                 time += min(tickets[i], tickets[k] - 1)

#         return time

# s=Solution()
# tickets = [2,3,2]
# k = 2
# print(s.timeRequiredToBuy(tickets,k))




# class Solution(object):
#     def timeRequiredToBuy(self, tickets, k):
#         time = 0
#         for i in range(len(tickets)):
#             if i <= k:
#                 time += min(tickets[i], tickets[k])
#                 print(time)
#             else:
#                 time += min(tickets[i], tickets[k] - 1)
#                 print(time)

#         return time
# s=Solution()
# tickets = [5,1,1,1,1]
# k = 2
# print(s.timeRequiredToBuy(tickets,k))


