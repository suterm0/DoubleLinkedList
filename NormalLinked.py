# Michael Suter
# Normal linked list
# 3-4-20


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None  # Sets head value to None
        self.tail = None

    def add_to_head(self, data):    # data represents the lists info
        new_node = Node(data)    # Creates a new node and imports the data from it
        new_node.next = self.head   # Sets the pointer to the new node
        self.head = new_node    # adds the new_node to the head of the Linked list

    def add_to_end(self, data):
        new_node = Node(data)  # Creates a new node and imports the data from it
        current = self.head
        while current.next:    # This while loop checks to see where the last value in the list is
            current = current.next
            if current is None:
                current = new_node

    def push_end(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def contains(self, value):
        current = self.head
        while current.next:
            if current.data == value:
                return True
            current = current.next
            if current.data == value:
                return True
            else:
                return False

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data

    def clear(self):  # Sets the head value to none, thus clearing the list
        self.head = None

    def remove_value(self, value):
        previous_node = None
        current = self.head
        while current:
            if current.data() == value:
                if previous_node:
                    previous_node.next(current.new_node())
                else:
                    self.head = current.next()
                return
            previous_node = current
            current = current.next
        return False
