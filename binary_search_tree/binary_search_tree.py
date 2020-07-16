"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left 
            # if we see that there is no left child, to compare the input value to, 
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's insert method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see there is no right child,
            if self.right is None:
                # then we can wrap the value in a BSTNode and we park 
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's insert method
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare the input(target) with the value of the node
        # if the value equal the root node
        if self.value == target:
            return True
            # return true
        # if value is < than the node's value
        if target < self.value:
            # go left
            # if no left child
            if not self.left:
                # then does not exist
                return False
            else:
                # call `contains` on the left child 
                return self.left.contains(target)    
        # otherwise, value is > than the node's value
        else:
            # go right
            # if no right child
            if not self.right:
                return False
            else:
                return self.right.contains(target) 
        

    # Return the maximum value found in the tree
    def get_max(self):
        # keep going right until there isn't another node to go to, that last node is the highest node
        # create a var that stores the current node
        current = self
        # if the current node has a right child
        # set current to the right child
        while current.right is not None:
            current = current.right
        # once the right most leaf is reached that will be the greatest value
        return current.value
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the anonymous function on `self.value`
        fn(self.value)

        # if this node has a left child 
        if self.left:
            # pass the anonymous fn to it 
            self.left.for_each(fn)
        # if this node has a right child 
        if self.right:
            # pass the anonymous fn to it 
             self.right.for_each(fn)
             

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
