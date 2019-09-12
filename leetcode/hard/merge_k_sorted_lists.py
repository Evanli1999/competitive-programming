import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        return self.first < other.first

    def tostr(self):
        return "(" + str(self.first) + ", " + str(self.second) + ")"

class Solution:
    def mergeKLists(self, lists):
        res = ListNode(0)
        heap = []
        for i, lst in enumerate(lists):
            heapq.heappush(heap, Pair(lst.val, i))

        tail = res
        while not not heap:
            p = heapq.heappop(heap)
            val, smallest = p.first, p.second

            tail.next = lists[smallest]
            tail = tail.next

            if lists[smallest].next:
                lists[smallest] = lists[smallest].next
                heapq.heappush(heap, Pair(lists[smallest].val, smallest))

        return res.next
