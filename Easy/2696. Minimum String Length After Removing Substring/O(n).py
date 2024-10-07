class Solution:
    def minLength(self, s: str) -> int:
        palavra = []

        for letra in s:
            try:
                if letra == "B" and palavra[-1] == "A":
                    palavra.pop()
                elif letra == "D" and palavra[-1] == "C":
                    palavra.pop()
                else:
                    palavra.append(letra)
            except:
                palavra.append(letra)
        
        return(len(palavra))
