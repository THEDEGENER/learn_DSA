import random

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class BinaryTree():
    def __init__(self, head=None):
        self.head = head
        
    def convert_list(self, list: list) -> function:
        """Takes in a list which must be sorted for a binary tree. The functions traverses from the mid
            and sets the pointer of left and right to recursivly be the middle"""
        sorted_list = sorted(list)
        def convert(start, end):
            if start > end: # these values will come together recursivly as we shift the start and end
                return None
            mid = (start + end) // 2
            return TreeNode(sorted_list[mid], convert(start, mid - 1), convert(mid + 1, end))
        
        return convert(0, len(sorted_list) - 1)
    
    def traverse(self, root: TreeNode) -> None:
        """Recursivly prints the left and right nodes value in sorted order, swap left and right to get decending"""
        if root:
            self.traverse(root.left)

            print(root.val)

            self.traverse(root.right)
        
            
    def find_num(self, num, tree):
        """Traverses the tree and prints if the number is found"""
        current = tree
        while current is not None:
            if current.val == num:
                print(f"number {num} found in tree!")
                return None
            current = current.left if current.val > num else current.right
        else:
            print("num not found")
    
arr = [random.randint(0, 100) for _ in range(100)]
tree = BinaryTree()
converted_tree = tree.convert_list(arr)
tree.traverse(converted_tree)
tree.find_num(random.randint(1, 100), converted_tree)
