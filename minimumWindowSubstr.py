class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        char_count_s = { s[i]:0 for i in range(len(s))}
        char_count_t = Counter(t)
        left = 0
        start_idx = -1
        min_window = float("inf")
        count = 0
        for right in range(len(s)):
            if not s[right] in char_count_t:
                continue
            
            char_count_s[s[right]] += 1
            if char_count_s[s[right]] <= char_count_t[s[right]]:
                count += 1
            
            if count == len(t):
                while char_count_s[s[left]] > char_count_t[s[left]] or (not char_count_s[s[left]]):
                    if char_count_s[s[left]] > char_count_t[s[left]]:
                        char_count_s[s[left]] -= 1
                    left += 1

                len_of_window = right - left + 1
                if min_window > len_of_window:
                    min_window = len_of_window
                    start_idx = left
        if start_idx == -1:
            print("No window found")
            return
        return s[start_idx: start_idx + min_window]


# Python3 program to find the smallest window
# containing all characters of a pattern.
    def findSubString(self,string, pat):

        len1 = len(string)
        len2 = len(pat)


        no_of_chars = 256
        # check if string's length is less than pattern's
        # length. If yes then no such window can exist
        if len1 < len2:

            print("No such window exists")
            return ""

        hash_pat = [0] * no_of_chars
        hash_str = [0] * no_of_chars

        # store occurrence ofs characters of pattern
        for i in range(0, len2):
            hash_pat[ord(pat[i])] += 1

        start, start_index, min_len = 0, -1, float('inf')

        # start traversing the string
        count = 0  # count of characters
        for j in range(0, len1):

            # count occurrence of characters of string
            hash_str[ord(string[j])] += 1

            # If string's char matches with
            # pattern's char then increment count
            if (hash_pat[ord(string[j])] != 0 and
                            hash_str[ord(string[j])] <=
                            hash_pat[ord(string[j])]):
                count += 1

            # if all the characters are matched
            if count == len2:

                # Try to minimize the window i.e., check if
                # any character is occurring more no. of times
                # than its occurrence in pattern, if yes
                # then remove it from starting and also remove
                # the useless characters.
                while (hash_str[ord(string[start])] >
                                    hash_pat[ord(string[start])] or
                                    hash_pat[ord(string[start])] == 0):

                    if (hash_str[ord(string[start])] >
                                            hash_pat[ord(string[start])]):
                        hash_str[ord(string[start])] -= 1
                    start += 1

                # update window size
                len_window = j - start + 1
                if min_len > len_window:

                    min_len = len_window
                    start_index = start

        # If no window found
        if start_index == -1:
            print("No such window exists")
            return ""

        # Return substring starting from
        # start_index and length min_len
        return string[start_index: start_index + min_len]

sln = Solution()
print(sln.minWindow("ADOBECODEBANC", "ABC"))
