class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None
        self.prev = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            current = self.head
            while current and current.priority >= priority:
                current = current.next
            if current is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            elif current == self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                previous = current.prev
                previous.next = new_node
                new_node.prev = previous
                new_node.next = current
                current.prev = new_node

    def remove(self):
        if self.head is None:
            return None
        highest_priority_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return highest_priority_node.value

    def peek(self):
        elements = []
        current = self.head
        while current:
            elements.append((current.value, current.priority))
            current = current.next
        return elements
