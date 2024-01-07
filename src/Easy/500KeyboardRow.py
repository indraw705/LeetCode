from typing import List

class Solution:
    def check_keyboard(word, lane):
        for i in word:
            if i in lane:
                continue
            else:
                return False
                break
        return True

    def findWords(self, words: List[str]) -> List[str]:
        matching_words = []
        lane_1 = "qwertyuiopQWERTYUIOP"
        lane_2 = "asdfghjklASDFGHJKL"
        lane_3 = "zxcvbnmZXCVBNM"
        compare_lane = ""
        for word in words:
            if word[0] in lane_1:
                if Solution.check_keyboard(word, lane_1):
                    matching_words.append(word)
            elif word[0] in lane_2:
                if Solution.check_keyboard(word, lane_2):
                    matching_words.append(word)
            else:
                if Solution.check_keyboard(word, lane_3):
                    matching_words.append(word)

        return matching_words


obj=Solution()
print(obj.findWords(["Hello","Alaska","Dad","Peace"]))
print(obj.findWords( ["omk"]))
print(obj.findWords(["adsdf","sfd"]))