from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        matriz = []

        intervals.sort()

        matriz.append(intervals[0])

        for par in intervals[1:]:
            entrou = True
            for grupo in matriz:
                if grupo[0] > par[0] and grupo[0] > par[1]:
                    grupo[0] = par[0]
                    entrou = False
                    break
                elif grupo[1] < par[0] and grupo[1] < par[1]:
                    grupo[1] = par[1]
                    entrou = False
                    break
            
            if entrou:
                matriz.append(par)
                
        print(intervals)
        print(matriz)

        return len(matriz)