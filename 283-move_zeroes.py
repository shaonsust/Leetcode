from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        This two pointer solution
        """
        l, r = 0, len(nums) - 1
        n = r
        while (l <= r):
            if nums[l] == 0:
                nums.insert(n, nums.pop(l))
                r -= 1
            else:
                l += 1

        return nums
    

    def move_zeroes(self, nums: List[int], target: int) -> None:
        pass


if __name__ == '__main__':
    for i in range(int(input())):
        arr = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.moveZeroes(arr))
