class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printNode(self,head):
        current = head
        while current:
            print(current.data)
            current = current.next

    def addNode(self,head,data):
        new_node = Node(data)
        new_node.next = head
        self.head = new_node

    def addNodeTail(self,head,data):
        new_node = Node(data)
        current = head
        print("current node is", current)
        while current.next != None:
            current = current.next
        print(current)
        current.next = new_node
        print(current.next)
        new_node.next = None


    def deleteNode(self,head,data):
        current = head
        print("head data is ", head.data)

        while current:
            if head.data == data: #head node
                head.data = None
                self.head = head.next
                break
            else:
                if current.next.data == data and current.next.next != None:  #middle node
                    print("current.next.data is ", current.next.data, current.next, current.next.next)
                    current.next.data = None
                    current.next = current.next.next
                    break
                elif current.next.data == data and current.next.next == None:  #tail node
                    current.next = None
                    break
            current = current.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    llist.addNodeTail(llist.head, 2)
    llist.addNodeTail(llist.head, 3)
    llist.addNodeTail(llist.head, 4)
    llist.addNodeTail(llist.head, 5)
    llist.addNodeTail(llist.head, 6)
    llist.addNodeTail(llist.head, 7)

    llist.printNode(llist.head)
    llist.deleteNode(llist.head, 1)
    llist.printNode(llist.head)
    llist.deleteNode(llist.head, 5)
    llist.deleteNode(llist.head, 7)
    llist.printNode(llist.head)