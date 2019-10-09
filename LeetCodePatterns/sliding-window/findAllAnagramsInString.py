class Solution:
    def findAllAnagrams(self, s, p):
        from collections import Counter
        lookup_p = Counter(p)
        left = 0
        right = 0
        sol = []
        word_size = len(p)
        counter = len(lookup_p)

        while right < len(s):
            if s[right] in lookup_p:
                lookup_p[s[right]] -= 1
                if lookup_p[s[right]] == 0:
                    counter -= 1
            right += 1
            
            if counter == 0:
                while counter == 0:
                    if right - left == word_size:
                        sol.append(left)
                    if s[left] in lookup_p:
                        lookup_p[s[left]] += 1
                        if lookup_p[s[left]] > 0:
                            counter += 1
                    left += 1
        return sol

sln = Solution()
print(sln.findAllAnagrams("cbaebabacd","abc"))
 