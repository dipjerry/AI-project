from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def alpha_beta_pruning(node, alpha, beta, maximizing_player):
    if node.is_terminal_node():
        return node.value

    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta_pruning(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta_pruning(child, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pruning', methods=['POST'])
def pruning():
    # Get the input values from the form
    data = request.get_json()
    alpha = float(data['alpha'])
    beta = float(data['beta'])

    # Perform the alpha-beta pruning algorithm
    result = alpha_beta_pruning(root_node, alpha, beta, True)

    # Return the result to the frontend
    return jsonify(result=result)

if __name__ == '__main__':
    root_node = Node(4)
    node_b = Node(7) 
    node_c = Node(2)
    node_d = Node(9)

    root_node.add_child(node_b)
    root_node.add_child(node_c)
    root_node.add_child(node_d)

    app.run(debug=True)
