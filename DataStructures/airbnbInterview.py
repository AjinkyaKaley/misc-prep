class QueueImp:
    def __init__(self):
        self.queue = []
    
    def enque(self,elem):
        
        if len(self.queue) == 0:
            new_arry = [elem]
            self.queue.append(new_arry)
            return 
        
        if len(self.queue[0]) < 5:
            self.queue[0].append(elem)
        elif len(self.queue[-1]) < 5:
            self.queue[-1].append(elem)
        else:
            self.queue.append([elem])
        
    
    def dequeue(self):
        if len(self.queue) == 0:
            return 
        
        self.queue[0].pop(0)
        if len(self.queue[0]) == 0:
            self.queue = self.queue[1:]
#         
# [[], [5, 6, 7, 8, 9]]
if __name__ == "__main__":
    q = QueueImp()
    for i in range(36):
        q.enque(i)
        
    print(q.queue)
    
    for i in range(36):
        q.dequeue()
    print(q.queue)
    # q.dequeue()
    print(q.queue)
    
        
    


# Queue: [1, 2, 3, 4, 5, 6, 7, 8, ...] in one array
# Limit for each array it can hold at max 5 elements
# Queue: [[1, 2, 3, 4, 5], [6, 7, 8,..]]

# 
# Your previous Plain Text content is preserved below:
# 
# // Build a queue class with the enqueue and dequeue methods. 
# // The queue can store an *UNLIMITED* number of elements but you are limited to using arrays that can store up to 5 elements max.

# [
#     1, 
#     2,
#     3,
#     4,
#     5
# ]

# Queue: [1, 2, 3, 4, 5, 6, 7, ...]
# To implement this queue, you can only use array as the data structure, and for each array that stores the element can only hold up to 5 elements at max

# array [1, 2, 3, 4, 5]
# array 1 , array 2, ....

# Queue: []
# enque(1)
# Queue: [1]
# enque(2)
# Queue: [1, 2]
# deque():
# Queue: [2]