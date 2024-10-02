from typing import List

# def menorDist(tempo1, tempo2):
#         volta = 1440
        
#         absMenos = abs(tempo1 - tempo2)
#         # absVolta = abs(volta - absMenos)
#         return(min(absMenos, absVolta))

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeMin = [60*int(i[0:2])+int(i[3:5]) for i in timePoints]
        timeMin.sort()
        
        tam = len(timeMin)
        
        menor = 1440 - (timeMin[-1] + timeMin[0])
        
        for i in range(tam-1):
            
            menor = min(menor, (timeMin[i+1] - timeMin[i]))
                        
            if menor == 0:
                return 0
        return menor
    
so = Solution()

# print(so.findMinDifference(["00:00","23:59","00:00"]))
print(so.findMinDifference(["01:01","02:01"]))