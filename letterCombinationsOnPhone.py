class Solution:
    def __init__(self):
        self.letterToDigitMapping = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8: 'tuv', 9:'wxyz'}

    def letterCombinations(self, digits: 'str') -> 'List[str]':

        if digits == "":
            return []

        if len(digits) == 1:
            return list(self.letterToDigitMapping[int(digits)])

        encodings = self.letterCombinations(digits[1:])
        multiplier = digits[0]
        multiplierEncoding = self.letterToDigitMapping[int(multiplier)]
        result = []
        for m in multiplierEncoding:
            for e in encodings:
                t = m+e
                result.append(t)

        return result

sln = Solution()
print(sln.letterCombinations('9'))