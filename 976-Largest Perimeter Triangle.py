from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            if (nums[i + 1] + nums[i + 2]) > nums[i]:
                return sum(nums[i:i + 3])
        return 0


if __name__ == '__main__':
    for i in range(int(input())):
        nums = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.largestPerimeter(nums=nums))
