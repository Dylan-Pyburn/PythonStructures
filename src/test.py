# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LL:
    def __init__(self, head=None):
        self.head = head

    def add(self, val: int):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    newList = None
    curr = newList
    
    if not l1: return l2
    if not l2: return l1
    
    while l1 and l2:
        newNode = ListNode()
        if l1.val <= l2.val:
            newNode.val = l1.val
            l1 = l1.next
        else:
            newNode.val = l2.val
            l2 = l2.next
        
        if not newList:
            newList = newNode
            curr = newList
        else:
            curr.next = newNode
            curr = curr.next
        
    while l1:
        curr.next = ListNode(l1.val)
        curr = curr.next
        l1 = l1.next
        
    while l2 is not None:
        curr.next = ListNode(l2.val)
        curr = curr.next
        l2 = l2.next
        
    return newList
    
l1 = LL()
l1.add(4)
l1.add(2)
l1.add(1)

l2 = LL()
l2.add(4)
l2.add(3)
l2.add(1)

mergeTwoLists(l1.head, l2.head)