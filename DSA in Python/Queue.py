# In python, queue can be implemenyed using list, collections.deque or queue class

#1 Using list

stock_price_queue=[]

stock_price_queue.insert(0,131.10)
stock_price_queue.insert(0,132.10)
stock_price_queue.insert(0,135)

print(stock_price_queue)

print(stock_price_queue.pop())
#first in element has exited first ✅

#Using deque

from collections import deque
q=deque()

q.appendleft(100)
q.appendleft(200)
q.appendleft(300)
print(q)