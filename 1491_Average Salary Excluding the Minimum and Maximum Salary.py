from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary)  - 2)


if __name__ == '__main__':
    for i in range(int(input())):
        salary = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.average(salary=salary))
