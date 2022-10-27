class Solution:
    bad = 0

    def __init__(self, bad) -> None:
        self.bad = bad
        
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        ans = 0

        while(left <= right):
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def isBadVersion(self, version: int) -> bool:
        return version >= self.bad


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        bad = int(input())

        obj = Solution(bad)
        print(obj.firstBadVersion(n))
