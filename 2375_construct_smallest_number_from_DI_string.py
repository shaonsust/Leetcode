class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num, flag = [], True

        for i in range(len(pattern) + 1):
            num.append(i+1)

        while flag:
            cnt = 0
            for i in range(len(pattern)):
                if pattern[i] == "D":
                    if num[i] < num[i+1]:
                        num[i], num[i+1] = num[i+1], num[i]
                        cnt += 1
                
                if pattern[i] == "I":
                    if num[i] > num[i+1]:
                        num[i], num[i+1] = num[i+1], num[i]
                        cnt += 1
            if cnt == 0:
                flag = False

        return "".join(map(str, num))


if __name__ == '__main__':
    obj = Solution()
    
    for _ in range(int(input())):
        pattern = input()
        obj = Solution()
        print(obj.smallestNumber(pattern=pattern))
