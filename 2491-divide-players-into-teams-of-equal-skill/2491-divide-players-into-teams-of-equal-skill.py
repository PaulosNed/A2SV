class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start = 0
        end = len(skill) - 1
        ans = 0
        totalSkill = skill[start] + skill[end]
        while(end > start):
            currSkill = skill[start] + skill[end]
            if currSkill != totalSkill:
                return -1
            ans += (skill[start] * skill[end])
            end -= 1 
            start += 1
        return ans