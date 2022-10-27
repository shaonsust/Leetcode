from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            palindrom = word[::-1]
            if palindrom == word:
                return palindrom

        return ""


words = []
for i in range(int(input())):
    str = input()
    words.append(str)

obj = Solution()
print(obj.firstPalindrome(words))
