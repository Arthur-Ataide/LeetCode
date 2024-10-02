from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        vetOrdenado = sorted(list(set(arr)))

        Dict = {}

        for i in range(len(vetOrdenado)):
            Dict[vetOrdenado[i]] = i + 1

        return list(map(lambda x: Dict[x], arr))