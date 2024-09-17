from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tam = len(nums)

        for i in range(tam):
            for j in range(i, tam):
                if j != i:
                    alvo = nums[i] + nums[j]

                    if alvo == target:
                        return i, j
        
solution = Solution()
    
print(solution.twoSum([3,2,4], 6))