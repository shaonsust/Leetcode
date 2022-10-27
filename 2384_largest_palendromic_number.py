from typing import List


class Solution:
    def largestPalindromic(self, num: List[int]) -> List:
        ans = []
        flag = 0
        max_ind = -10
        temp = [0] * 10
        sorted_num = [int(x) for x in num]

        for i in sorted_num:
            temp[i] += 1
        
        for i, val in enumerate(temp):
            if val % 2 > 0:
                max_ind = i
            
            if val > 1:
                if val % 2 == 0:
                    for j in range(val):
                        if j % 2 == 0:
                            ans.insert(0, i)
                        else:
                            ans.insert(len(ans), i)
                else:
                    for j in range(val - 1):
                        if j % 2 == 0:
                            ans.insert(0, i)
                        else:
                            ans.insert(len(ans), i)
        
        if ans and len(ans) > 0:
            if ans[0] == 0:
                ans.clear()
                if max_ind < 0 and flag == 0:
                    ans.insert(len(ans) // 2, 0)

        if max_ind >= 0:
            ans.insert(len(ans) // 2, max_ind)

        return ''.join([str(x) for x in ans])


if __name__ == '__main__':
    for _ in range(int(input())):
        num = input()
        obj = Solution()
        print(obj.largestPalindromic(num))
