class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        dict1 = {}
        l=[]
        for i in range(len(messages)):
            if senders[i] in dict1:
                dict1[senders[i]] = dict1.get(senders[i]) + (messages[i].count(" "))+1
            else:
                dict1[senders[i]] = (messages[i].count(" "))+1
        x=max(dict1.values())
        for k,v in dict1.items():
            if v==x :
                l.append(k)
        if len(l)==1:
            return l[0]
        else:
            l=sorted(l)[::-1]      #Lexigograhical sorting of list
            return l[0]


obj01 = Solution()
print(obj01.largestWordCount(["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"],
                             ["Alice", "userTwo", "userThree", "Alice"]
                             ))

print(obj01.largestWordCount(
    ["l", "E", "e", "L", "U", "B", "H", "H", "l", "I", "E", "c", "s", "t", "s", "u", "r", "F", "Q", "v", "K", "x", "M",
     "r", "o", "k", "o", "E", "x", "f"],
    ["TYproPIptp", "ZinKBnptgb", "MabHvYDOvr", "KJsXlcnoLX", "IMjvhaCNQU", "qWTfyhzuge", "CBCPpuHdKb", "HpDxmDTUwp",
     "SgOTFxFYpl", "PctQGYkMuz", "KqAEViZnnc", "DVTKOJLZPc", "InJQqHsICO", "bNhncDzkLu", "IvbKSkMTWM", "nOjJjZjQTa",
     "ekqBBwyCYb", "zADZhwSwFj", "LswFXzVDyF", "bhIcpZBHWb", "mesrFSlmqJ", "OZZKylOPUj", "OVDIlCRBro", "IIhwLrjgHo",
     "HrXZYYiXnT", "pmHsmhKLoB", "ppIkHHnBqQ", "gNGHfhhxEL", "VSZuisvhuQ", "qaPorTEGcL"]
))
