class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        vetor = []

        for letra in s:
            try:
                if vetor[-1] == "(" and letra == ")":
                    vetor.pop()
                
                else:
                    vetor.append(letra)        
            except:
                vetor.append(letra)
        
        return len(vetor)