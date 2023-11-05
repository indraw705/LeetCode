# https://leetcode.com/problems/decode-the-message/description/
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decr_key = ""
        for ch in key:
            if ch not in decr_key:
                decr_key += ch
        decr_key = decr_key.replace(" ", "") + " "
        out = ""
        alfa = "abcdefghijklmnopqrstuvwxyz "
        for char in message:
            out += alfa[decr_key.index(char)]

        return out


obj = Solution()
print(obj.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
