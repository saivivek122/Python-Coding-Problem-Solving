class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traversal(head):
        curnode = head
        




a = ListNode(11)
b = ListNode(12)
c = ListNode(13)

a.next = b
b.next = c

print(a.data)
print(a.next.data)
print(a.next.next.data)
