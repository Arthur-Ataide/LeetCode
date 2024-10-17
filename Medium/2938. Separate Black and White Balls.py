from typing import Counter


class Solution:
    def minimumSteps(self, s: str) -> int:
        counter = Counter(s)
        tam = len(s)

        tam0 = counter['0']
        
        cont = tam0
        index = -1
        movimentos = 0

        for i in range(tam-tam0):
            index = s[index+1:].index("1") + index + 1
            movimentos += cont - index
            cont += 1

        return movimentos
