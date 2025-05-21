import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        maior = float('-inf')
        heap = []
        
        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0))
            maior = max(maior, nums[i][0])
        
        vetorDist = [float('-inf'), float('inf')]

        while heap:
            menor, indexVet, index = heapq.heappop(heap)

            # [a, b] [c,d]
            # if b - a < d - c or a < c if b - a == d - c

            # [menor, maior] [vetorDist[0],vetorDist[1]]
            if maior - menor < vetorDist[1] - vetorDist[0] or maior - menor == vetorDist[1] - vetorDist[0] and menor < vetorDist[0]:
                vetorDist = [menor, maior]
            
            if index + 1 < len(nums[indexVet]):
                prox = nums[indexVet][index+1]
                heapq.heappush(heap, (prox, indexVet, index+1))
                maior = max(maior, prox)
            
            else:
                break

        return vetorDist

        return [0]
