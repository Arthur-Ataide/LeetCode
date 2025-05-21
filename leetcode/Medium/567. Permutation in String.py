from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counterS1 = Counter(s1)
        tamS1 = len(s1)

        for i in range(len(s2)-tamS1+1):
            # print(Counter(s2[i:tamS1]))
            # print(counterS1)
            # print()
            if Counter(s2[i:tamS1+i]) == counterS1:
                return True
        
        return False
