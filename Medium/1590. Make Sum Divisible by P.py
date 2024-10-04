from typing import List
# achei dificil

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        resto = total % p

        if resto == 0:
            return 0

        tam = len(nums)
        tamTotal = tam
        dici = {0: -1}
        soma = 0

        for i, num in enumerate(nums): # pega o indice "i" e o vlaor do "vetor[i]"
            soma += num
            mod = soma % p
            alvo = (mod - resto + p) % p

            if alvo in dici:
                tam = min(tam, i - dici[alvo])

            dici[mod] = i
        
        print(dici)
        return tam if tam < tamTotal else -1

        
