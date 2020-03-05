#Michael Suter
# Stack method / add or remove from the end
# 3-5-20

from NormalLinked import LinkedList


class Stack:
    def __init__(self):
        self.the_stack = []

    def push(self, data):
        self.the_stack.append(data)

    def pop(self):
        return


class Queue(LinkedList):
    def __init__(self):
        self.myList = LinkedList.__init__(self)

    def push(self, data):
        self.myList.push_end(data)

    def pop(self):
        self.myList.remove_head()
