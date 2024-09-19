# Hash Table / Math / String

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000,}
        
        soma = 0
        tam = len(s)
        
        for i in range(tam):
            atual = dict[s[i]]
            if(i != tam-1):
                prox = dict[s[i+1]]
                
                if atual >= prox:
                    soma += atual
                else:
                    soma -= atual
            else:
                soma += atual
        
        return soma
            
solucao = Solution()

print(solucao.romanToInt('IV'))