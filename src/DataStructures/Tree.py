class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)


# Creating a tree
root = Node("mahadev")

child1 = Node("Vijay")
child2 = Node("BHARAT")
child3 = Node("Kalpana")

child4 = Node("triveni")
child5 = Node("shri")
child6 = Node("indra")
child7 = Node("shrenika")
child8 = Node("shrijit")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(child4)
child1.add_child(child5)

child2.add_child(child7)
child2.add_child(child8)

child3.add_child(child6)


# Traversing the tree and printing in a tree-like structure
def traverse(node, level=0):
    print("  " * level + "- " + node.data)
    for child in node.children:
        traverse(child, level + 1)

# Call the traverse function with the root node
traverse(root)
