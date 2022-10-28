from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        pass


if __name__ == '__main__':
    for _ in range(int(input())):
        nums = [int(x) for x in input().split()]
        k = int(input())

        obj = Solution()
        print(obj.subarrayGCD(nums=nums, k=k))
