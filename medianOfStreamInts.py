import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
            return

        if len(self.maxHeap) == len(self.minHeap):
            if self.minHeap[0] < num:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        elif len(self.maxHeap) > len(self.minHeap):
            if self.minHeap and num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                top = -heapq.heappop (self.maxHeap)
                heapq.heappush(self.minHeap, top)
                heapq.heappush(self.maxHeap, -num)
        else:
            if  self.maxHeap and num < self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                top = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -top)
                heapq.heappush(self.minHeap, num)

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.maxHeap) == len(self.minHeap):
            upper, lower = -self.maxHeap[0], self.minHeap[0]
            print((upper+lower)//2)
            return (upper+lower)//2
        elif len(self.maxHeap) > len(self.minHeap):
            print(-self.maxHeap[0])
            return -self.maxHeap[0]
        else:
            print(self.minHeap[0])
            return self.minHeap[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
