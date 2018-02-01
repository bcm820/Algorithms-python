
class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

class SList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.count += 1
        return self

    def add_front(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            node.next = self.head
            self.head = node
        self.count += 1
        return self
    
    def remove_last(self):
        if not self.head:
            return None
        else:
            ptr = self.head
            while ptr.next is not self.tail:
                ptr = ptr.next
            node = ptr.next
            ptr.next = None
            self.tail = ptr
            self.count -= 1
            return node
    
    def remove_front(self):
        if not self.head:
            return None
        elif self.head.next:
            node = self.head
            self.head = self.head.next
            self.count -= 1
            return node
        else:
            node = self.head
            self.head = None
            self.count -= 1
            return node

    def remove_node(self, value):
        if not self.head:
            return None
        else:
            ptr = self.head
            if ptr.value is value:
                return self.remove_front()
            while ptr.next:
                if ptr.next.value is value:
                    node = ptr.next
                    if ptr.next.next:
                        ptr.next = ptr.next.next
                    else:
                        ptr.next = None
                    self.count -= 1
                    return node
                ptr = ptr.next
            return None

    def find(self, value):
        if not self.head:
            return None
        else:
            ptr = self.head
            if ptr.value is value:
                return ptr
            while ptr.next:
                if ptr.next.value is value:
                    return ptr.next
                ptr = ptr.next
            raise ValueError(f'Error: Node with value "{value}" not found.')
    
    def find_previous(self, value):
        if not self.head:
            return None
        else:
            ptr = self.head
            if ptr.value is value:
                return None # if no parent, but head, then head must be target value!
            while ptr.next:
                if ptr.next.value is value:
                    return ptr
                ptr = ptr.next
            raise ValueError(f'Error: Node with value "{value}" not found.')

    def insert_before(self, node, value):
        if not self.head:
            raise ValueError(f'Error: Linked list is empty! Use add(value) to add a node.')
        else:
            current = self.find_previous(node)
            if not current:
                return self.add_front(value)
            else:
                before = Node(value)
                before.next = current.next
                current.next = before
                return self

    def insert_after(self, node, value):
        if not self.head:
            raise ValueError(f'Error: Linked list is empty! Use add(value) to add a node.')
        else:
            before = self.find(node)
            after = Node(value)
            after.next = before.next
            before.next = after
            return self

    def display(self):
        if not self.head:
            return self
        else:
            ptr = self.head
            print(ptr.value)
            while ptr.next:
                print(ptr.next.value)
                ptr = ptr.next
            return self