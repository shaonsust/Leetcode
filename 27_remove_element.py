import time
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    k: int = 0
    l: int = len(nums)

    for i in range(l):
        if nums[i] == val:
            nums[i] = -1
            k += 1

    nums.sort(reverse=True)
    return l - k


def remove_element_two_pointer(nums: List[int], val: int) -> int:
    i = 0
    j = len(nums) - 1
    k = 0

    while i < j:
        if nums[i] == val:
            nums[i] = -1
            k += 1

        if nums[j] == val:
            nums[j] = -1
            k += 1
        i += 1
        j -= 1

    nums.sort(reverse=True)
    return len(nums) - k


if __name__ == '__main__':
    for _ in range(int(input())):
        nums = [int(x) for x in input().split()]
        val = int(input())
        # start_time = time.time()
        print("k1 ===> ", remove_element(nums, val))
        # print("elapsed time one ==> ", time.time() - start_time)

        # start_time = time.time()
        # print("k2 ===> ", remove_element_two_pointer(nums, val))
        # print("elapsed time two ==> ", time.time() - start_time)
