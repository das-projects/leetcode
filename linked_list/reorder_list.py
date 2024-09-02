# 143. Reorder List
# Link: https://leetcode.com/problems/reorder-list/
# Difficulty: Medium
# Question: You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# Constraints:
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # merge the two halves
        first = head
        second = prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            temp = second.next
            second.next = first
            second = temp
        