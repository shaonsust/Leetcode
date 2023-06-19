from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        k: int = 0

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 200
                k += 1

        nums.sort()
        return len(nums) - k
    
    def remove_duplicates_two_pointer(self, nums: List[int]) -> int:
        k: int = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        
        return k
    
    def remove_duplicates_set(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)


if __name__ == '__main__':
    for _ in range(int(input())):
        nums = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.remove_duplicates_set(nums=nums))
