class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        idx = 0
        # self.result = [0]*len(A)

        self.carry = 0
        for i in range(len(A)):
            if A[i] == 0:
                A.popleft()
        arr = self.helper(A, idx)
        if self.carry > 0:
            arr.append(self.carry)
        return reversed(arr)

    def helper(self, A, idx):
        if idx == len(A)-1:
            total = A[idx] + 1
            if total >= 10:
                self.carry = total // 10
                total = total % 10
            return [total]
        total_sum = []
        total_sum += self.helper(A, idx+1)
        curr_idx_sum = A[idx] + self.carry
        if curr_idx_sum >= 10:
            self.carry = curr_idx_sum // 10
            total_sum += [curr_idx_sum % 10]
        else:
            total_sum += [curr_idx_sum]
            self.carry = 0
        return total_sum

sln = Solution()
sln.plusOne([0,0,1, 9, 9, 9, 9, 9, 9])
