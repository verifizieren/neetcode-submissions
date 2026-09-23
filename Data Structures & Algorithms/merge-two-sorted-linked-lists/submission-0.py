# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = list1, list2
        res = None
        tail = None

        while left and right:
            if left.val <= right.val:
                pick = left
                left = left.next
            else:
                pick = right
                right = right.next

            if res is None:
                res = pick
                tail = pick
            else:
                tail.next = pick
                tail = tail.next

        while left:
            if res is None:
                res = left
                tail = left
            else:
                tail.next = left
                tail = tail.next
            left = left.next

        while right:
            if res is None:
                res = right
                tail = right
            else:
                tail.next = right
                tail = tail.next
            right = right.next

        return res