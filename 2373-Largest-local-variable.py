from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = []
        for i in range(n-2):
            temp = []
            for j in range(n-2):
                mx = 0
                for k in range(i, i+3):
                    mx = max(mx, max(grid[k][j:j+3]))
                temp.append(mx)
            maxLocal.append(temp)
        return maxLocal

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = []
        print([0]*n)
        ans = [[0]*n for _ in range(n)]
        print(ans)

        for j in range(n):
            grid.append([int(k) for k in input().split()])
        print(len(grid))
        obj = Solution()
        print(obj.largestLocal(grid))
