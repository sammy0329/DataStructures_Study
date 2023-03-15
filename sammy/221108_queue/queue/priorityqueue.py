from queue import PriorityQueue
# put(), get() 함수는 O(log n)
q = PriorityQueue()

q.put(4)
q.put(1)
q.put(7)
q.put(3)

print(q.get())  
print(q.get())  
print(q.get())  
print(q.get())  