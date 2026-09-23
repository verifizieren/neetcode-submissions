class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth = self.getHeadOrKth(head, k)
        dummy = kth
        while head and not (head is kth):
            new_head = self.flipK(head, k)
            kth = self.getHeadOrKth(new_head, k)
            head.next, head = kth, new_head
        return dummy

    def getHeadOrKth(self, head, k):
        cur = head
        while (k - 1) > 0 and cur:
            cur = cur.next
            k -= 1
        return cur or head

    def flipK(self, head, k):
        prv, cur = None, head
        while k > 0:
            prv, cur = cur, self.flip(prv, cur)
            k -= 1
        return cur

    def flip(self, prv, cur):
        nxt, cur.next = cur.next, prv
        return nxt
