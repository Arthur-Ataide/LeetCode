from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        tam = len(nums)

        max = 0

        for i in range(tam):
            for j in range(i, tam):
                x = nums[i]
                y = nums[j]
                if (i != j and abs(x - y) <= min(x,y)):
                    xor = x ^ y
                    if (max < xor):
                        max = xor
        
        return(max)

        



