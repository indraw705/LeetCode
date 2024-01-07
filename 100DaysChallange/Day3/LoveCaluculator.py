class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n = n-1
                if n == 0:
                    return True
                else:
                    flowerbed[i]=1
        return False

obj1 = Solution()
print(obj1.canPlaceFlowers([1,0,0,0,1], n = 1))