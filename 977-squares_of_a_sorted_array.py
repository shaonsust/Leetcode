from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * (right + 1)
        ind = right

        while left <= right:
            if (abs(nums[left]) >= abs(nums[right])):
                res[ind] = nums[left]**2
                left += 1
            else:
                res[ind] = nums[right]**2
                right -= 1
            
            ind -= 1

        return res


if __name__ == '__main__':
    for i in range(int(input())):
        nums = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.sortedSquares(nums))
