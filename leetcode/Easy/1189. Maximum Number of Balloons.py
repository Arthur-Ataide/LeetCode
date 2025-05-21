# Hash Table / String / Counting

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon
        palavra = 'baon'
        quant = Counter(text)
        menor = quant['l']//2
        
        for i in palavra:
            valor = quant[i]
            if i == 'o':
                valor = valor//2
                
            if menor > valor:
                menor = valor
        return menor
        
        
solucao = Solution()

print(solucao.maxNumberOfBalloons('nlaebolko'))