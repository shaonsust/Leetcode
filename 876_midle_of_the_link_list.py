from typing import Optional


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def midleNode(self, head:Optional[Node]) -> Optional[Node]:
        temp = head
        cnt = 0

        while temp:
            temp = temp.next
            cnt += 1
        
        mid = (cnt // 2)
        
        while mid:
            head = head.next
            mid -= 1
        
        return head
    
    def middleNode1(self, head:Optional[Node]) -> Optional[Node]:
        arr = [head]
        while arr[-1].next:
            print(arr[-1].val)
            arr.append(arr[-1].next)
        
        return arr[len(arr) // 2]

    def middleNode2(self, head:Optional[Node]) -> Optional[Node]:
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next
        
        return arr[len(arr) // 2]
    
    def middleNode3(self, head:Optional[Node]) -> Optional[Node]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


if __name__ == '__main__':
    for i in range(int(input())):
        arr = [int(x) for x in input().split()]
        head = Node(arr[0])
        temp = head

        for j in range(1, len(arr)):
            node = Node(arr[j], None)
            temp.next = node
            temp = node
        
        obj = Solution()
        ans_node = obj.middleNode2(head)

        while ans_node:
            print(ans_node.val)
            ans_node = ans_node.next

