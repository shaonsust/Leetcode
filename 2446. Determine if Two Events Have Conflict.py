from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if (event2[0] <= event1[0] <= event2[1]) or (event1[0] <= event2[0] <= event1[1]):
            return True
        else:
            return False


if __name__ == '__main__':
    for _ in range(int(input())):
        event1 = [str for str in input().split()]
        event2 = [str for str in input().split()]

        obj = Solution()
        print(obj.haveConflict(event1=event1, event2=event2))

