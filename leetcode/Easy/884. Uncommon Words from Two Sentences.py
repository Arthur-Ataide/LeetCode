# Hash Table / String / Counting

from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        vet = []

        s1 = s1.split()
        s2 = s2.split()

        palavras = s1 + s2

        counter = Counter(palavras)

        for palavra in counter:
            if counter[palavra] == 1:
                vet.append(palavra)

        return vet
 
solution = Solution()
    
print(solution.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))