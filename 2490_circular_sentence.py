class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        str_list = sentence.split()
        for i in range(1, len(str_list)):
            if str_list[i][0] != str_list[i-1][-1]:
                return False        

        return True


if __name__ == '__main__':
    for i in range(int(input())):
        sentence = input()
        obj = Solution()
        print(obj.isCircularSentence(sentence=sentence))
