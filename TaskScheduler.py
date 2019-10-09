class Solution:

    def taskScheduler(self, task, n):
        
        if n == 0:
            return len(task)

        from collections import Counter
        import heapq

        count = Counter(task)
        heap = []
        for task, freq in count.items():
            heap.append((-freq, 0, task))
            
        heapq.heapify(heap)
        current_time = 0
        scheduleTask = []
        cycleCount = 0
        temp = []
        while heap:
            scheduleTask = []
            temp = []
            while heap:
                freq, scheduleTime, task = heapq.heappop(heap)
                if scheduleTime <= current_time:
                    scheduleTask.append(task)
                    freq *= -1
                    freq -= 1
                    scheduleTime += (n + 1)
                    temp.append((-freq, scheduleTime, task))
                    # current_time += 1
                    # heapq.heappush(heap, (-freq, scheduleTime, task))
                else:
                    temp.append((freq, scheduleTime, task))
                    # heapq.heappush(heap, (freq, scheduleTime, task))
            # if len(scheduleTask) == n:
            
            for freq,scheduleTime,task in temp:
                if (freq*-1) > 0:
                    heapq.heappush(heap, (freq, scheduleTime, task))
            cycleCount += len(scheduleTask) if scheduleTask else 1
            current_time = cycleCount
        return cycleCount

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        from heapq import heappop, heappush
        curr_time, h = 0, []
        for k, v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x, y = heappop(h)
                    if x != -1:
                        temp.append((x+1, y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return curr_time


sln = Solution()
# sln.taskScheduler(["A", "A", "A", "B", "B", "B"], n=2)
print(sln.taskScheduler(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
                  2))

