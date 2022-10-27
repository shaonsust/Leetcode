class Solution:
    def backtracking_algorithm(self, list, s):
        if list == 1:
            return s
        else:
            return [ 
                y + x
                for y in self.backtracking_algorithm(1, s)
                for x in self.backtracking_algorithm(list - 1, s)
            ]
    
    def practice(self):
        permute = [y + x for y in ["a", "b", "c"] for x in ["a", "b", "c"]]
        temp = []

        for y in ["a", "b", "c"]:
            for x in ["a", "b", "c"]:
                temp.append(y+x)
        
        print(temp)


if __name__ == '__main__':
    obj = Solution()
    obj.practice()

    print(obj.backtracking_algorithm(1, ["a","b","c"]))
    print(obj.backtracking_algorithm(2, ["a","b","c"]))
    # print(obj.backtracking_algorithm(3, ["a","b","c"]))
