from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        tam = len(nums)
        
        for i in range(tam-1, -1, -1):
            for j in range(tam-i):
                if (nums[j] <= nums[i+j]):
                    return i