class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Dummy node acts as a starting point for the merged list
        dummy = ListNode(-1)
        current = dummy

        # Traverse both lists and append the smaller node to the merged list
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes of list1 or list2, if any
        current.next = list1 if list1 else list2

        return dummy.next
