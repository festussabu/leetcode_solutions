# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    curr = head
    lst = []
    sorted_nodes = []

    while curr:
        lst.append(curr)
        curr=curr.next

    left = 0
    right = len(lst) - 1
    while left <= right:
        sorted_nodes.append(lst[left])
        left +=1 
        sorted_nodes.append(lst[right])
        right-=1
        
    head = sorted_nodes[0]
    for i in range(len(sorted_nodes) - 1):
        sorted_nodes[i].next = sorted_nodes[i+1]
    sorted_nodes[-1].next = None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
        
reorderList(head)
curr = head
while curr:
    print(curr.val)
    curr = curr.next

