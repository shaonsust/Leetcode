from typing import List


class Solution():
    def majority_element(self, nums: List[int]) -> int:
        nums.sort()
        flag = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                flag += 1
                if flag > len(nums)//2:
                    return nums[i]
            else:
                flag = 1
        return nums[0]
    
    def majority_element1(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[len(nums)//2]
        return a


if __name__ == '__main__':
    for _ in range(int(input())):
        nums = [int(x) for x in input().split()]
        obj = Solution()
        print(obj.majority_element1(nums=nums))
