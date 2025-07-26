# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node_list = []
        carry = 0
        p1 = l1
        p2 = l2
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            new_node = ListNode(total % 10)
            node_list.append(new_node)
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0] if node_list else None
    
def array_to_linkedList(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedList_to_array(l1):
    node_list = []
    current_node = l1
    while current_node:
        node_list.append(current_node.val)
        current_node = current_node.next
    return node_list

if __name__ == "__main__":
    l1 = array_to_linkedList([2,3,4])
    l2 = array_to_linkedList([3,4,5])
    sol = Solution()
    result = linkedList_to_array(sol.addTwoNumbers(l1, l2))
    print(result)