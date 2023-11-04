class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        commonChar = strs[0]
        for word in strs:
            if word.startswith(commonChar):
                continue
            else:
                strs[0] = commonChar[:-1]
                return self.longestCommonPrefix(strs)

        return commonChar


obj01 = Solution()
print(obj01.longestCommonPrefix(['flower', 'flow', 'flight']))
print(obj01.longestCommonPrefix(["dog", "racecar", "car"]))
print(obj01.longestCommonPrefix(["indrajit", "india", "indie", "indonesia"]))
