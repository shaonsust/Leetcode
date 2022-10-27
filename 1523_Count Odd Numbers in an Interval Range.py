import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0 or high % 2 != 0:
            return (high - low) // 2 + 1
        
        return (high - low) // 2

    def countOdds1(self, low: int, high: int) -> int:
        return (math.ceil(high / 2) - math.trunc(low / 2))


if __name__ == '__main__':
    for i in range(int(input())):
        low = int(input())
        high = int(input())

        obj = Solution()
        print(obj.countOdds1(low, high))
        print(math.ceil(high / 2))
        print("low ==> " + str(low) + " ===> ", math.trunc(low / 2))

