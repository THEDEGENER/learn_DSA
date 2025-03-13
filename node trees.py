

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

        def append(self, new_node):
            # define the current node as the head node
            current = self.head
            # if the current has a value of true meaning it contains a node
            if current:
                # then we assign the .next node to be the current node which we then define as the next node
                while current.next:
                    current = current.next
                current.next = new_node
            # else if the current value has no head node then the new_node becomes the head node starting off the list 
            else:
                self.head = new_node

        # def a class to delete a new node by checking if the node to delete is the first node and if true the second node becomes the next node
        # otherwise we have to keep track of the previous node and the next node to join them together
        def delete(self, value):
            # delete the first node with a given value
            current = self.head
            # here we take the value of the current node and if its equal to the value we passed to the method to delete then the head node becomes the
            # next node
            if current.value == value:
                self.head = current.next
            else:
                while current:
                    if current.value == value:
                        break
                    prev = current
                    current = current.next
                if current == None:
                    return
                prev.next = current.next
                current = None
                



# initialize nodes with thier value

e1 = Node(1)
e2 = Node(2)

# we can define the head node by passing a node to the LinkedList class which will initialize it as a head node
ll = LinkedList(e1)
# e1 becomes out head node
