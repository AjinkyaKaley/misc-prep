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

    def rearrangeStringOptimal(self, s, k):
        if k == 0:
            return s
        counter = collections.Counter(s)
        queue = [[-counter[char], char] for char in counter]
        heapq.heapify(queue)
        mem = collections.deque()
        current = ""
        res = ''
        while len(queue) or len(mem):
            if len(mem) == k:
                current = mem.popleft()
                if current[0] < 0:
                    heapq.heappush(queue, current)
            if len(queue):
                current = heapq.heappop(queue)
                res += current[1]
                current[0] += 1
                mem.append(current)
            else:
                if sum([item[0] for item in mem]) == 0:
                    return res
                else:
                    return ''

sln = Solution()
print(sln.rearrangeStringOptimal("aaabc", 3))
