from typing import Counter


class Solution:
    def maximumSwap(self, num: int) -> int:
        lista = list(str(num))

        cont = Counter(lista)

        tamJ = len(lista)
        tamI = 0
        for i in range(9, -1, -1):
            if (cont[str(i)]) > 0:
                for j in range(tamJ):
                    numero = str(i)
                    if (lista[j] < numero):
                        index = tamJ - lista[::-1].index(numero) - 1
                        if index > j:
                            lista[index] = lista[j]
                            lista[j] = numero
                            return int(''.join(lista))
                        break
        return num
        
        
