# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        list_nums = []
        
        while head !=None:
            list_nums.append(head.val)
            head = head.next
            
        list_nums = sorted(list_nums)
            
        answerList = ListNode(0)
        
        result = answerList
        
        for num in list_nums:
            answerList.next = ListNode(num)
            answerList = answerList.next
         
        return result.next