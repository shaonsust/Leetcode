import string


class Solution:
    # 2's compliment solution
    def hammingWeight(self, n: int) -> int:
        unsign_int = n + 2**32

        return bin(unsign_int).count('1') - 1

    
    # Using Bitwise left shift(<<) operator
    def hammingWeight1(self, n: int) -> int:
        unsign_int = n + (1 << 32)

        return bin(unsign_int).count('1') - 1
    

if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())

        obj = Solution()
        print(obj.hammingWeight1(n))
