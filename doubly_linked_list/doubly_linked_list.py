"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # check if list is empty
        if self.head is None:
            # set new node to head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # set the new node's next to current head
            new_node.next = self.head
            # set the current head to point back now to the new node
            self.head.prev = new_node
            # set new node to be the new head
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        current = self.head
        # check if head has a next value
        if current.next is not None:
            # remove connection between current and next
            current.next.prev = None
            # set new head to the current head's next node
            self.head = current.next
        else:  # if head.next is None
            # remove only node in the list
            self.head = None
            self.tail = None
        
        self.length -= 1
        return current.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        # check if list is empty
        if self.head is None:
            # set new node to head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # set new node's previous to current tail
            new_node.prev = self.tail
            # set current tail's next to new node
            self.tail.next = new_node
            # set new node as new tail
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current = self.tail
        # only decrement length if it is greater than zero
        if self.length > 0:
            self.length -= 1
        # check if tail has prev value
        if current.prev is not None:
            # remove connection of current tail to it's prev node
            current.prev.next = None
            # declare the current tail's prev the new tail
            self.tail = current.prev
        else:  # if length is 1
            # remove only node in the list
            self.head, self.tail = None, None
        return current.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # remove node from list and store in variable for later
        new_head = self.delete(node)
        # add saved variable to head of the list
        self.add_to_head(new_head)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # remove node from list & store in variable for later
        new_tail = self.delete(node)
        # add saved variable to end of the list
        self.add_to_tail(new_tail)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # list is empty
        if self.length == 0:
            return

        self.length -= 1
        # list only has one node
        if self.head is self.tail:
            self.head, self.tail = None, None
            return node.value

        # delete head
        elif node is self.head:
            self.head = self.head.next
            node.next, self.head.prev = None, None
            return node.value

        # delete tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.prev, self.tail.next = None, None
            return node.value

        # delete from middle
        else:
            # prev, node (current node being deleted), next
            # prev = current node's prev // next = current node's next
            prev, next = node.prev, node.next
            # prev.next = current node's next // next.prev = current node's prev
            prev.next, next.prev = node.next, node.prev
            # So they are cutting out the current node
            return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # current is like a counter of nodes.
        current = self.head
        max = 0

        while current is not None:
            # if the amount of nodes counted(current) is above max
            if current.value > max:
                # make max = the current
                max = current.value
                # then go to the next node, making the current go up one until there is no more nodes and current == max
            current = current.next

        return max