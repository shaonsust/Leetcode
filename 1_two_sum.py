from operator import le
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two pointer solution, Complexity O(n)
        """
        l, r = 0, len(nums) - 1
        temp_nums = sorted(nums)

        while l < r:
            temp = temp_nums[l] + temp_nums[r]

            if temp == target:
                try:
                    l = nums.index(temp_nums[l])
                    r = nums.index(temp_nums[r], l + 1, len(nums))  # if vlaue not find, will throw a value error
                except ValueError:
                    r = nums.index(temp_nums[r], 0, l + 1, )

                return [l, r]

            if temp < target:
                l = l + 1
            else:
                r = r - 1

        return []

    def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
        """
        HashMaps Solution, complexity O(n)
        """
        seen = {}
        for i, value in enumerate(nums):
            req_value = target - value
            if req_value in seen:
                return [seen[req_value], i]
            seen[value] = i

    def twoSumHashMap1(self, nums: List[int], target: int) -> List[int]:
        """
        HashMaps Solution, complexity O(n)
        """
        for i, value in enumerate(nums):
            rem = target - value

            if rem in nums[i + 1:]:
                return [i, nums[i + 1:].index(rem) + (i + 1)]


if __name__ == '__main__':
    for i in range(int(input())):
        nums = [int(x) for x in input().split()]
        target = int(input())

        obj = Solution()
        print(obj.twoSumHashMap1(nums, target))
