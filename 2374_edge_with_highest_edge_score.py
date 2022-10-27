from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        temp_edges = [0] * len(edges)
        
        for i, val in enumerate(edges):
            temp_edges[val] += i
        
        return temp_edges.index(max(temp_edges))


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        edges = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.edgeScore(edges=edges))
