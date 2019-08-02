class Solution:
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     low = 0
    #     high = len(matrix)-1
    #     return self.BSinMatrix(matrix, target, low, high)

    # def BSinMatrix(self, matrix, target, low, high):

    #     while low <= high:
    #         mid = (low + high) // 2
    #         rangeLow = 0
    #         rangeHigh = len(matrix[0])-1
    #         if target >= matrix[mid][rangeLow] and target <= matrix[mid][rangeHigh]:
    #             if self.BSinArray(matrix[mid], target, rangeLow, rangeHigh):
    #                 return True
    #             # elif low == high:
    #             #     return False
    #         if mid > 0 and target < matrix[mid][rangeHigh]:
    #             high = mid-1
    #         else:
    #             low = mid+1
    #     return False

    # def BSinArray(self, _array, target, low, high):
    #     print(_array)
    #     while low <= high:
    #         mid = low + (high-low) // 2
    #         if _array[mid] == target:
    #             return True
    #         if _array[mid] > target:
    #             high = mid-1
    #         elif _array[mid] < target:
    #             low = mid+1
    #     return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right-left)//2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)

        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)

sln = Solution()

sln.searchMatrix(
    # [[-5]]
    [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

, 22)
