import copy
class NextGreatestElement:

    def Nge(self, nums):
        stack = copy.deepcopy(nums)
        result = [-1]
        ngeValue = stack.pop()

        for i in range(len(nums)-2,0, -1):
            topOfStack = stack.pop()
            if topOfStack > ngeValue:
                ngeValue = topOfStack
            elif topOfStack < ngeValue and topOfStack < nums[i+1] and i+1 != len(nums)-1:
                ngeValue = -1
            result.append(ngeValue)

        if stack.pop() > ngeValue:
            result.append(-1)
        else:
            result.append(ngeValue)

nge = NextGreatestElement()
nge.Nge([4,5,2,25])
