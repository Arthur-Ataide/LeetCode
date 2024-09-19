# Linked List / Math / Recursion


from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: List[ListNode], l2: List[ListNode]) -> List[ListNode]:
        
        
        # l1 = ''.join(map(str, l1))[::-1]
        # l2 = ''.join(map(str, l2))[::-1]
        
        # l3 = int(l1) + int(l2)
        # l3 = list(str(l3)[::-1])
        
        return l1[0].next
        
        
solucao = Solution()

print(solucao.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))

