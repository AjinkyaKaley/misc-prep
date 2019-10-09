class Solution:

    # def minWindow(self, s, t):
    #     from collections import Counter
    #     char_count_s = {s[i]: 0 for i in range(len(s))}
    #     char_count_t = Counter(t)
    #     left = 0
    #     start_idx = -1
    #     min_window = float("inf")
    #     count = 0
    #     for right in range(len(s)):
    #         if not s[right] in char_count_t:
    #             continue

    #         char_count_s[s[right]] += 1
    #         if char_count_s[s[right]] <= char_count_t[s[right]]:
    #             count += 1

    #         if count == len(t):
    #             while char_count_s[s[left]] > char_count_t[s[left]] or (not char_count_s[s[left]]):
    #                 if char_count_s[s[left]] > char_count_t[s[left]]:
    #                     char_count_s[s[left]] -= 1
    #                 left += 1

    #             len_of_window = right - left + 1
    #             if min_window > len_of_window:
    #                 min_window = len_of_window
    #                 start_idx = left
    #     if start_idx == -1:
    #         print("No window found")
    #         return
    #     return s[start_idx: start_idx + min_window]

    def minWindowSubstr(self, s, t):
        from collections import Counter
        lookup_t = Counter(t)
        left = 0
        right = 0
        res = float("inf")
        ans = ""
        counter = len(lookup_t)

        while right < len(s):
            if s[right] in t:
                lookup_t[s[right]] -= 1
                if lookup_t[s[right]] == 0:
                    counter -= 1
            right += 1
            if counter == 0:
                
                while counter == 0:
                    if right - left < res:
                        res = right - left
                        ans = s[left:right]

                    _c = s[left]
                    if _c in lookup_t:
                        lookup_t[_c] += 1
                        if lookup_t[_c] > 0:
                            counter += 1
                    left += 1
        return ans

sln = Solution()
print(sln.minWindowSubstr("ADOBECODEBANC","ABC"))