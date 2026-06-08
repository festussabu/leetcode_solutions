class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    prev = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next

        prev = prev.next
    if list1:
        prev.next = list1
    else:
        prev.next = list2
    return dummy.next
            
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

list1 = create_linked_list([1,2,4])
list2 = create_linked_list([1,3,4])
result = mergeTwoLists(list1, list2)

curr = result
while curr:
    print(curr.val)
    curr = curr.next
