from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        sum = -900000000

        for i in nums:
            curr = curr + i
            if curr > sum:
                sum = curr
            
            if curr < 0:
                curr = 0
        
        return sum


if __name__ == '__main__':
    for i in range(int(input())):
        nums = [int(x) for x in input().split()]
        
        obj = Solution()
        print(obj.maxSubArray(nums))
