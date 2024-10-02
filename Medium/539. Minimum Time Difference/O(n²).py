from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeMin = [60*int(i[0:2])+int(i[3:5]) for i in timePoints]
        
        tam = len(timeMin)
        
        menor = abs(timeMin[0] - timeMin[-1])
        max = 1440
        print(timeMin)
        
        for i in range(tam):
            for j in range(i+1, tam):
                absMenos = abs(timeMin[i] - timeMin[j])
                absVolta = abs(max - absMenos)
                
                # print(timeMin[i], timeMin[j])
                
                if menor > absMenos or menor > absVolta:
                    if absMenos > absVolta:
                        menor = absVolta
                    else:
                        menor = absMenos
                        
                    if menor == 0:
                        return 0
        return menor
    
so = Solution()

print(so.findMinDifference(["00:00","23:59","00:00"]))
# print(so.findMinDifference(["01:01","02:01"]))