from typing import Counter, List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        tam = len(arr)

        vetResto = [i % k for i in arr]
        counter = Counter(vetResto)

        for resto in counter:
            if resto == 0:
                if counter[resto] % 2 != 0:
                    return False
            else:
                if counter[resto] != counter[k-resto]:
                    return False
        
        return True

        # for i in range(tam//2):
        #     try:
        #         num = resto[0]
        #         resto.pop(0)

        #         if num == 0:
        #             resto.pop(resto.index(0))

        #         else:
        #             resto.pop(resto.index(k-num))

        #     except:
        #         return False
            
        # return True
