from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        sum_energy = sum(energy) + 1
        if (sum_energy - initialEnergy) > 0:
            ans = sum_energy - initialEnergy

        for val in experience:
            if (val+1) > initialExperience:
                ans = ans + ((val - initialExperience) + 1)
                initialExperience = val + 1
            initialExperience += val
        
        return ans
        

if __name__ == '__main__':
    for _ in range(int(input())):
        initial_energy = int(input())
        initial_experience = int(input())
        energy = [int(x) for x in input().split()]
        experience = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.minNumberOfHours(initialEnergy=initial_energy, initialExperience=initial_experience, energy=energy, experience=experience))
