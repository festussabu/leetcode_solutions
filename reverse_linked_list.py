class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

                
h = [1,2,3,4,5]
head = ListNode(h[0])
head.next = ListNode(h[1])
head.next.next = ListNode(h[2])
head.next.next.next = ListNode(h[3])
head.next.next.next.next = ListNode(h[4])

curr = reverseList(head)
while curr:
    print(curr.val, end="->")
    curr = curr.next


