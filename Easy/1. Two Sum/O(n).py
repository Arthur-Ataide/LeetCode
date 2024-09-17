from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        
        tam = len(nums)
        
        for i in range(tam):
            dict[nums[i]] = i

        for i in range(tam):
            complemento = target - nums[i]
            if complemento in nums and dict[complemento] != i:
                return i, dict[complemento]
        
solution = Solution()
    
print(solution.twoSum([3,2,4], 6))