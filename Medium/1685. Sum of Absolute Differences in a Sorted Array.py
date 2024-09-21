# Array / Math / Prefix Sum

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        tam = len(nums)
        # vet = [[0 for i in range(tam)] for j in range(tam)]
        vet = []
        dict = {}
        total = sum(nums)
        totalmenor =[]
        totalmenor.append(0)

        for i in range(0, tam):
            totalmenor.append(nums[i]+totalmenor[i])

        for i in range(tam):
            num = nums[i]
            if (num not in dict):
                mult1 = nums[i]*i
                mult2 = nums[i]*(tam - i)
                valor = abs(totalmenor[i] - mult1) + abs(-totalmenor[i]+total - mult2)
                dict[num] = valor
                vet.append(valor)
            else:
                vet.append(dict[num])
                
        return(vet)

        

solucao = Solution()

print(solucao.getSumAbsoluteDifferences([1,4,6,8,10]))
print(solucao.getSumAbsoluteDifferences([2,3,5]))
