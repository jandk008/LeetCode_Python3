from leetcode.linked_list import ListNode


class Solution(object):
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        length = len(head)
        k = length - k % length
        previous, new_head, current = ListNode(0), ListNode(0), head
        while current:
            if k == 1:
                new_head = current
            k -= 1
            previous = current
            current = current.next
        previous.next = head
        head = new_head.next
        new_head.next = None
        return head
