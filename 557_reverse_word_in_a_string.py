from hashlib import new


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]

        return ' '.join(arr)


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()

        obj = Solution()
        print(obj.reverseWords(s))
