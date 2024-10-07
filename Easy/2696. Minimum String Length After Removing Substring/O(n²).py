class Solution:
    def minLength(self, s: str) -> int:
        tam = len(s)
        while(True):
            trocou = 1
            s = s.replace("AB", "")
            s = s.replace("CD", "")

            tamanho = len(s)
            if tamanho == tam:
                print(s)
                return tam
            
            tam = tamanho
