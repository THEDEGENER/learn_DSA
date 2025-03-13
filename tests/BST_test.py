from binary_search_tree import *
import random

arr = [random.randint(0, 100) for _ in range(100)]
tree = BinaryTree()
converted_tree = tree.convert_list(arr)
tree.traverse(converted_tree)
tree.find_num(random.randint(1, 100), converted_tree)


