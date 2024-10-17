from heapq import heappop, heappush
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        tam = len(times)

        ordenado = sorted(range(len(times)), key = lambda x: times[x][0])  
        cadeirasVazias = list(range(tam))
        cadeirasUtilizadas = []            

        for vetor in ordenado:                                                
            sentou, levantou = times[vetor]

            while cadeirasUtilizadas and cadeirasUtilizadas[0][0] <= sentou:
                heappush(cadeirasVazias, heappop(cadeirasUtilizadas)[1])
            cadeira = heappop(cadeirasVazias)                                  

            if vetor == targetFriend: return cadeira

            heappush(cadeirasUtilizadas,(levantou, cadeira))     



    
    # def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    #     tam = len(times)

    #     entrada = times[targetFriend][0]

    #     times = [[times[i][0], times[i][1], i] for i in range(tam)]

    #     times = sorted(times, key = lambda x:x[0])

    #     cadeira = 0
    #     aux = 0
    #     vetorCadeira = [0 for i in range(tam)]
    #     print(times)

    #     for i in range(tam):
    #         if times[i][2] == targetFriend:
    #             if cadeira < 0:
    #                 return 0
    #             return vetorCadeira.index(0)
            
    #         else:
    #             if times[i][1] > entrada:
                    
    #                 # try: 
                        
    #                 if times[i-1][1] < times[i][1]:
    #                     cadeira = vetorCadeira.index(0) + aux
    #                     vetorCadeira[cadeira] = 1
    #                     aux = 0

    #                 # except:
    #                 else:
    #                     cadeira = vetorCadeira.index(0)
    #                     vetorCadeira[cadeira] = 1
    #                     cadeira+=1
    #             else:
    #                 aux += 1
    #         print(vetorCadeira)

    