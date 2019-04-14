class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret

sln = Solution()
print(sln.longestCommonPrefix(["flower","flow","flight"]))