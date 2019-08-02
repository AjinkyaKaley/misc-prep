
class K:
    def __init__(self, obj,cmp):
        self.obj = obj
        self.mycmp = cmp;

    def __lt__(self, other):
        return self.mycmp(self.obj, other.obj) < 0

    def __gt__(self, other):
        return self.mycmp(self.obj, other.obj) > 0

    def __eq__(self, other):
        return self.mycmp(self.obj, other.obj) == 0

    def __le__(self, other):
        return self.mycmp(self.obj, other.obj) <= 0

    def __ge__(self, other):
        return self.mycmp(self.obj, other.obj) >= 0

    def __ne__(self, other):
        return self.mycmp(self.obj, other.obj) != 0

class Solution:
    def comparator(self,a, b): 
        ab = str(a) + str(b) 
        ba = str(b) + str(a) 
        return ((int(ba) > int(ab)) - (int(ba) < int(ab))) 
      

    def biggestNumberByConcat(self, items):
        items = [K(i, self.comparator) for i in items]
        temp = sorted(items)
        return temp

sln = Solution()
sln.biggestNumberByConcat([54, 546, 548, 60])