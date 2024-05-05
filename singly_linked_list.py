// AI Scrivener //
// Creator by : hafizhhasyhari //
# %% Definitions
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return self

    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._length -= 1
        if not self._length:
            self.tail = None
        return former_head.value

    def pop_right(self):
        if not self._length:
            raise Exception("list is empty")
        former_tail_value = self.tail.value
        current_node = self.head
        if self._length > 1:
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        else:
            self.head = self.tail = None
        self._length -= 1
        return former_tail_value

    def remove(self, value):
        if not self._length:
            raise Exception("list is empty")
        if self.head.value is value:
            return self.pop_left()
        node_prev = self.head
        node = self.head.next
        while node.value is not value and node is not None:
            node_prev = node
            node = node.next
        if node is None:
            raise Exception("value not found")
        if node.next is None:
            return self.pop_right()
        node_prev.next = node.next
        node.next = None
        self._length -= 1
        return node.value

    def reverse(self):
        # none, a, b, c, d
        l = None
        m = self.head
        while m is not None:
            r = m.next
            m.next = l
            l = m
            m = r
        self.head, self.tail = self.tail, self.head
        return self


# %% Scrips
x = SinglyLinkedList()
x.prepend(4)
x.prepend(3)
x.prepend(2)
x.prepend(1)
x.reverse()
# x.remove(4)
# x.remove(1)
# x.remove(3)
# x.head.value
# x.head
# x.tail.value
i = x.head
while i is not None:
    print(i.value)
    i = i.next
