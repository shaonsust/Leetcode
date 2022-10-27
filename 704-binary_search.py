from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        nums = [int(x) for x in input().split()]
        target = int(input())

        obj = Solution()
        print(obj.search(nums, target))
