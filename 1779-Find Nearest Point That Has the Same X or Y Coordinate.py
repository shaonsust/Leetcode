from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        temp = 99999
        idx = -1

        for i, arr in enumerate(points):
            if x == arr[0] or y == arr[1]:
                md = abs(x - arr[0]) + abs(y - arr[1])
                if md < temp:
                    idx = i
                    temp = md
        return idx


if __name__ == '__main__':
    for i in range(int(input())):
        x = int(input())
        y = int(input())
        
        points = []
        n = int(input())
        for j in range(n):
            points.append([int(x) for x in input().split()])
        
        obj = Solution()
        print(obj.nearestValidPoint(x, y, points=points))
