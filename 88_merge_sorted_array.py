from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0

        while i < m and j < n:
            if nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                j = j + 1
                m = m + 1
            
            i = i + 1
        
        if j < n:
            for x in range(j, n):
                nums1.insert(m, nums2[x])
                m = m + 1

        for i in range(len(nums1) - 1, m - 1, -1):
            nums1.pop(i)
        
        print(nums1)


    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
        
        nums1[:n] = nums2[:n]
        
        print(nums1)


if __name__ == '__main__':
    for i in range(int(input())):
        nums1 = [int(x) for x in input().split()]
        m = int(input())

        nums2 = [int(x) for x in input().split()]
        n = int(input())

        obj = Solution()
        obj.merge1(nums1, m, nums2, n)
