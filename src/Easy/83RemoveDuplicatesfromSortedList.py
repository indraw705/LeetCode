# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head

        curr = head
        while curr.next != None:
            if curr.val == curr.next.val:
                # tmp = curr.next
                curr.next = curr.next.next
                # del tmp
            else:
                curr = curr.next
        return head


# listnode
# obj = Solution()
# print(obj.deleteDuplicates([1,2,3]))
# # print(obj.deleteDuplicates([1,1,2,2,3,4,5,6,7,8,9,9]))
# # print(obj.deleteDuplicates([]))