from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur


    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node


    def print_list(self):
        cur = self.head
        while cur:
            print(str(cur.data) + ' <----> ',end='')
            cur = cur.next

dll1 = DoublyLinkedList()
dll1.append(2)
dll1.append(4)
dll1.append(5)
dll1.append(7)
dll1.append(8)
dll1.prepend(0)

dll1.print_list()


