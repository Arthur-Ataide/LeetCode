# Hash Table / Math / Sorting / Counting / Enumeration

from collections import Counter 

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        # vet = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16384', '32768', '65536', '131072', '262144', '524288', '1048576', '2097152', '4194304', '8388608', '16777216', '33554432', '67108864', '134217728', '268435456', '536870912']
        vet = [str(2**i) for i in range(30)]

        count = Counter(str(n))

        for i in range(30):
            if(count == Counter(vet[i])):
                return(True)

        return(False)


solucao = Solution()

print(solucao.reorderedPowerOf2(679213508))

print(2**30)