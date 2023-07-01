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

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("this is not valid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count =count + 1

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next

        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    # ll.print()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(19)
    # ll.insert_at_end(17)
    # ll.insert_at_beginning(20)
    # ll.insert_at_end(9)
    ll.insert_values(["indra", "pranita", "shubham", "atul", "gayatri"])
    ll.print()
    ll.remove_at(-1)
    ll.print()
