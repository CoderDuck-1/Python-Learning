class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        else:
            llstring=""
            current_node = self.head
            while current_node != None:
                llstring += str(current_node.data)+"-->"
                current_node = current_node.next
            print(llstring)

    def insert_at_end(self, data):
            if self.head is None:
                node = Node(data, self.head)
                self.head = node
                return
            else:
                current_node = self.head
                while current_node.next is not None:
                    current_node = current_node.next
                node = Node(data, None)
                current_node.next = node

    def insert_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length

    def remove_element(self, index):
        if index < 0 or index >= self.get_length():
            print("Index out of range")
            return
        elif index == 0:
            self.head=self.head.next
            return
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            current_node.next = current_node.next.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            print("Index out of range")
            return
        elif index == 0:
            self.insert_at_beginning(data)
        elif index == self.get_length():
            self.insert_at_end(data)
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            node = Node(data, current_node.next)
            current_node.next = node

    def insert_after_value(self, data_after, data_to_insert):
        current_node = self.head
        while current_node.data != data_after:
            current_node = current_node.next
        node=Node(data_to_insert, current_node.next)
        current_node.next=node

    def remove_by_value(self, data_to_remove):
        count=0
        current_node = self.head
        while current_node is not None:
            if current_node.data == data_to_remove:
                self.remove_element(count)
                return
            elif count == self.get_length():
                print("Element not found")
            else:
                current_node = current_node.next
                count += 1








if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_list(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()