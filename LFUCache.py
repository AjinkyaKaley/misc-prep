import heapq

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.map = {}               # key to value
        self.freq_time = {}         # key to (freq, time)
        # (freq, time, key), only updated when new key is added
        self.priority_queue = []
        self.update = set()         # keys that have been get/put since last new key was added

    def get(self, key):
        self.time += 1

        if key in self.map:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time)
            self.update.add(key)
            return self.map[key]

        return -1

    def put(self, key, value):
        if self.capacity <= 0:
            return

        self.time += 1
        if not key in self.map:

            if len(self.map) >= self.capacity:      # must remove least frequent from cache

                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    # whilst (least frequent, oldest) needs to be updated, update it and add back to heap
                    _, _, k = heapq.heappop(self.priority_queue)
                    f, t = self.freq_time[k]
                    heapq.heappush(self.priority_queue, (f, t, k))
                    self.update.remove(k)

                # remove (least frequent, oldest)
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)

            self.freq_time[key] = (0, self.time)
            heapq.heappush(self.priority_queue, (0, self.time, key))

        else:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time)
            self.update.add(key)

        self.map[key] = value


["LFUCache", "put", "put", "get", "get", "get",
    "put", "put", "get", "get", "get", "get"]
[[3], [2, 2], [1, 1], [2], [1], [2], [3, 3], [4, 4], [3], [2], [1], [4]]
cache = LFUCache(3)

cache.put(2, 2)
cache.put(1, 1)
cache.get(2)
cache.get(1)
cache.get(2)
cache.put(3, 3)
cache.put(4, 4)
cache.get(3)
cache.get(2)
cache.get(1)
cache.get(4)

# #  returns 1
# cache.put(3, 3)
# # // evicts key 2
# cache.get(2)
# # // returns - 1 (not found)
# cache.get(3)
# # // returns 3.
# cache.put(4, 4)
# # // evicts key 1.
# cache.get(1)
# # // returns - 1 (not found)
# cache.get(3)
# # // returns 3
# cache.get(4)
# # // returns 4
