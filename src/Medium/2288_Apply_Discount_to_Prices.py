# https://leetcode.com/problems/apply-discount-to-prices/
class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        out = ""
        for word in sentence.split():
            if word.startswith("$") and not (word.endswith("$")) and not ("$" in (word[1:][:-1])):
                discounted_val = (int(word[1:]) - float(word[1:]) * discount / 100)
                out += "$" + str(format(discounted_val, '.2f')) + " "
            else:
                out += word + " "

        return out.strip()

obj = Solution()
print(obj.discountPrices("there are $1 $2 and 5$ candies in the shop", 50))
print(obj.discountPrices("$2$3 $10 $100 $1 200 $33 33$ $$ $99 $99999 $9999999999", 0))
