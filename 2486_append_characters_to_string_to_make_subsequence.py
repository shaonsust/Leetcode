class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pos = 0
        cnt = 0

        for i in t:
            if s.find(i, pos) == -1:
                return len(t) - cnt

            pos = s.find(i, pos)
            cnt += 1
            pos += 1

        return 0

    def twoPointer(self, s: str, t: str) -> int:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1

        return len(t) - j


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        t = input()

        obj = Solution()
        print(obj.appendCharacters(s=s, t=t))
