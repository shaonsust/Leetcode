class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, total = 1, 0
        
        while n / 10:
            mod = n % 10
            n = n // 10
            product = product * mod
            total = total + mod
        return product - total


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())

        obj = Solution()
        print(obj.subtractProductAndSum(n))
