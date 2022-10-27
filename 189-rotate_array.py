from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modyfy nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


if __name__ == '__main__':
    for i in range(int(input())):
        arr = [int(x) for x in input().split()]
        k = int(input())

        obj = Solution()
        print(obj.rotate(arr, k))
