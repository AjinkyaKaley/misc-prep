class Solution:
    def permutationStr(self, s1, s2):
        from collections import Counter
        lookup_p = Counter(s1)
        left = right = 0
        counter = len(lookup_p)
        while right < len(s2):
            if s2[right] in lookup_p:
                lookup_p[s2[right]] -= 1
                if lookup_p[s2[right]] == 0:
                    counter -= 1
                    
            right += 1
            while counter == 0:
                if right - left == len(s1):
                    return True
                _c = s2[left]
                if _c in lookup_p:
                    lookup_p[_c] += 1
                    if lookup_p[_c] > 0:
                        counter += 1
                left += 1
        return False

sln = Solution()
print(sln.permutationStr("ab", "eidbooo"))
