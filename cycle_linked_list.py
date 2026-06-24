class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    s = head
    f = head
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            return True
    return False

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next

curr = hasCycle(head)
while curr:
    if curr == True or curr == False:
        print(curr)
        break
    curr = curr.next



