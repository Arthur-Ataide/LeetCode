from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        num1 = skill[0]
        num2 = skill[-1]

        alvo = num1 + num2
        soma = num1 * num2

        for i in range(1, len(skill)//2):
            num1 = skill[i]
            num2 = skill[-i-1]
            if num1 + num2 == alvo:
                soma += num1 * num2
            
            else:
                return -1
        
        return soma
