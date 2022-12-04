class Solution:
    def pivotInteger(self, n: int) -> int:
        temp = [0] * (n + 1)
        temp[0] = 0
        sum = 0

        for i in range(1, n + 1):
            temp[i] = temp[i - 1] + i
        
        for i in range(n, 0, -1):
            sum += i
            if sum == temp[i]:
                return i
        
        return '-1'
    
    def pivotInteger1(self, n: int) -> int:
        a = (n * (n + 1)) // 2

        for i in range(n + 1):
            b, c = (i * (i - 1)) // 2, (i * (i + 1)) // 2
            if a - b == c:
                return i
        
        return '-1'


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        
        obj = Solution()
        print(obj.pivotInteger1(n))
