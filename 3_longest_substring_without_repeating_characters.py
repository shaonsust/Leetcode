class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            print(s[i])
        return s


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()

        obj = Solution()
        print(obj.lengthOfLongestSubstring(s))
