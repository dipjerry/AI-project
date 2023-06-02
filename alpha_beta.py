class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def is_terminal(self):
        return not self.children
    def evaluate(self):
        return self.value
    def generate_children(self):
        return self.children
def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()
    if maximizing_player:
        value = float("-inf")
        for child in node.generate_children():
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for child in node.generate_children():
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
# Example usage
# Create a sample game tree
root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
root.children = [node1, node2]
node1.children = [node3, node4]
node2.children = [node5]
# Run the alpha-beta pruning algorithm
alpha_value = float("-inf")
beta_value = float("inf")
depth_limit = 3
maximizing = True
result = alpha_beta(root, depth_limit, alpha_value, beta_value, maximizing)
print(f"The result of the Alpha-Beta Pruning algorithm is: {result}")
