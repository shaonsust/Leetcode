from typing import Optional


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head:Optional[Node], n:int) -> Optional[Node]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        
        l = len(arr)
        if l == n:
            head = head.next
            return head

        l = l - n - 1
        arr[l].next = arr[l].next.next

        return head

    def removeNthFromEnd1(self, head:Optional[Node], n:int) -> Optional[Node]:
        slow = fast = head

        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head


if __name__ == '__main__':
    for i in range(int(input())):
        arr = [int(x) for x in input().split()]
        n = int(input())

        head = Node(arr[0])
        temp = head

        for j in range(1, len(arr)):
            x = Node(arr[j])
            temp.next = x
            temp = x
        
        obj = Solution()
        ans = obj.removeNthFromEnd(head, n)
        while ans:
            print(ans.val)
            ans = ans.next
        