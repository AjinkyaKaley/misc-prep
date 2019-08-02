import heapq
import collections

class Solution(object):
    def rearrangeString(self, str, k):
        heap = [(-freq, char)
                for char, freq in collections.Counter(str).items()]
        heapq.heapify(heap)
        res = []
        while heap:
            freq, char = heapq.heappop(heap)
            if freq == 0:
                break
            queue = collections.deque()
            res.append(char)
            for j in range(k - 1):
                if len(res) == len(str):
                    return "".join(res)
                if not heap:
                    return ""
                fre, nex = heapq.heappop(heap)
                res.append(nex)
                if fre < 0:
                    queue.append((fre+1, nex))
            while queue:
                f, key = queue.popleft()
                if f != 0:
                    heapq.heappush(heap, (f,key))
            heapq.heappush(heap, (freq+1, char))
        return "".join(res)

sln = Solution()
print(sln.rearrangeString("aaadbbcc", 2))
