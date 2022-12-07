class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class SingleList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.link

    def add_beginning(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node

    def add_end(self, data):
        new_end_node = Node(data)
        if self.head is None:
            self.head = new_end_node
        else:
            n = self.head
            while n.link:
                n = n.link
            n.link = new_end_node


ll1 = SingleList()
ll1.add_beginning(10)
ll1.add_beginning(35)
ll1.add_beginning(256)
ll1.add_end(1)
ll1.add_end(34567)
ll1.print_list()
