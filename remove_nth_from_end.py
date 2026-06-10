class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr = head
    arr=[]
    while curr:
        arr.append(curr)
        curr = curr.next
    if len(arr) == 1:
        head = None
    else:
        arr.pop(-n)
        head = arr[0]
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        arr[-1].next = None
    
    return head

head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

n = 1
removeNthFromEnd(head, n)
curr = head
while curr:
    print(curr.val)
    curr = curr.next
