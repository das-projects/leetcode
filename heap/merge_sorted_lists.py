# 23. Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard
# Description:
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Check if the list is empty
        if not lists or len(lists) == 0:
            return None
        # Merge the lists using a divide and conquer approach
        # Time complexity: O(n log k) where n is the total number of nodes and k is the number of lists
        # Space complexity: O(n) where n is the total number of nodes
        while len(lists) > 1:
            temp = []
            # Merge pairs of lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            # Update the list of lists
            lists = temp

        return lists[0]

    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node
        # Merge the two lists
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        # Append the remaining nodes
        if l1:
            node.next = l1
        else:
            node.next = l2
        # Return the merged list
        return ans.next
