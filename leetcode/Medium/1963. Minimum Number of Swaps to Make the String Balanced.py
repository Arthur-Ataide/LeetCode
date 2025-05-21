import math


class Solution:
    def minSwaps(self, s: str) -> int:
        vetor = []

        for letra in s:
            try:
                if vetor[-1] == "[" and letra == "]":
                    vetor.pop()
                
                else:
                    vetor.append(letra)        
            except:
                vetor.append(letra)
        
        tam = len(vetor)/4
        
        return math.ceil(tam)
