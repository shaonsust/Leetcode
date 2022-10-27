from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        two pointer solution
        """
        l, r = 0, len(s) - 1
        while(l < r):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s


if __name__ == '__main__':
    for i in range(int(input())):
        str = [x for x in input().split()]

        obj = Solution()
        print(obj.reverseString(str))
