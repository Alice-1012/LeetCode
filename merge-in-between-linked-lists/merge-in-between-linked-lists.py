# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aStartIdx = a - 1 
        aStart = list1 
        while(aStartIdx > 0 and aStart.next): 
            aStart = aStart.next 
            aStartIdx -= 1 
            #끝점 기록 
        aEndIdx = b + 1 
        aEnd = list1 
        while(aEndIdx > 0 and aEnd.next): 
            aEnd = aEnd.next 
            aEndIdx -= 1 
            #시작점 연결 
        bStart = list2 
        aStart.next = bStart 
        bEnd = list2 
        while(bEnd.next): 
            bEnd = bEnd.next 
            #끝점 연결 
        bEnd.next = aEnd 
        return list1

