from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointer solution
        """
        l, r = 0, len(numbers) - 1
        
        while l < r:
            if (numbers[l] + numbers[r]) == target:
                return [l+1, r+1]
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                r -= 1
        
        return "Solution is not exist."
    
    def two_sum(self, numbers: List[int], target:int) -> List[int]:
        """
        Iterative Binary search solution
        """
        for idx in range(len(numbers)):
            new_target = target - numbers[idx]
            l, r = idx + 1, len(numbers) - 1

            while(l <= r):
                mid = l + (r - l) // 2
                if numbers[mid] == new_target:
                    return [idx+1, mid+1]
                
                if numbers[mid] < new_target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return "solution is not exist."


if __name__ == '__main__':
    for i in range(int(input())):
        arr = [int(x) for x in input().split()]
        target = int(input())

        obj = Solution()
        print(obj.twoSum(arr, target))
