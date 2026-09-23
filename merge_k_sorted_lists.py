import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i_lst, lst in enumerate(lists):
        if lst:
            heap.append((lst.val, i_lst, lst))
    heapq.heapify(heap)

    dummy = tail = ListNode()
    while heap:
        val, i_lst, node = heapq.heappop(heap)
        tail.next = node
        tail = node

        if node.next:
            heapq.heappush(heap, (node.next.val, i_lst, node.next))

    return dummy.next


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]


print(mergeKLists(lists))
