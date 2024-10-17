import heapq
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums.sort()

        heap = [-nums[i] for i in range(len(nums)-1, -1, -1)]

        soma = 0

        for i in range(k):
            numero = heapq.heappop(heap)
            soma += -numero

            heapq.heappush(heap, -ceil(-numero/3))
        
        
        return soma
