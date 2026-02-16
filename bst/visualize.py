from graphviz import Digraph


def visualize_tree(root, filename="bst_tree"):
    dot = Digraph()

    def add_nodes_edges(node):
        if node:
            dot.node(str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render(filename, view=True)
