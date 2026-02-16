from graphviz import Digraph

def visualize_tree(root, filename="bst_visual"):
    dot = Digraph()

    def add(node):
        if node:
            dot.node(str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add(node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add(node.right)

    add(root)
    dot.render(filename, view=True)

    