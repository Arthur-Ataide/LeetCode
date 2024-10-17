from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        tam = len(nums)
        pilha = []

        for i in range(tam):
            if not pilha or nums[pilha[-1]] > nums[i]:
                pilha.append(i)
        
        maior = 0

        for i in range(tam-1, -1, -1):
            while(pilha and nums[pilha[-1]] <= nums[i]):
                maior = max(maior, i - pilha.pop())

        return maior