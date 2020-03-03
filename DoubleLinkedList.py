#Michael Suter
#In this file there will be methods that are used in a double linked list
#3-3-20


class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_end(self):
        curr = self.head
        if curr is None:
            return

        while curr is not None:
            curr = curr.next

        curr.prev.next = None
        return curr.data

    def add_to_end(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            self.head.prev = None
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = None

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove_head(self):
        if self.head is None:
            return "Head is None"

        new_node = self.head
        self.head = new_node.next
        self.head.prev = None
        return new_node.data
