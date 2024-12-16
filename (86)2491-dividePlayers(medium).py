# 2491. Divide Players Into Teams of Equal Skill
# Oct 4, 2024
# Beats 10.13% Runtime
# Beats 6.21% Memory

class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        # Sum up array
        total = sum(skill)
        # If sum not divisible by number of pairs, return False
        if total % (len(skill) // 2) != 0:
            return -1
        skillLevel = total // (len(skill) // 2)

        d = {}
        # Add all numbers into dictionary as keys to their frequency
        for num in skill:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        # For each number in skill
            # Check if there is a value that completes the pair, and append to pairs. If there is ever not, return -1 
        pairs = []
        for num in skill:
            if d[num] > 0:
                if (skillLevel-num) in d and d[skillLevel-num] > 0:
                    d[num] -= 1
                    d[skillLevel - num] -= 1
                    pairs.append([ num, (skillLevel - num) ])
                else:
                    return -1
        
        # Sum up all skill levels
        totalSkill = 0
        for pair in pairs:
            totalSkill += (pair[0] * pair[1])

        return totalSkill
