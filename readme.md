# Water Jug Problem Solver ,  Language Detection and Alpha Beta Pruning

This repository contains three separate programs:

1. Water Jug Problem Solver: A Python program that solves the Water Jug problem using a breadth-first search (BFS) algorithm.

2. Language Detection: A Python program that detects the language of a given text using the langdetect library.

3. Alpha beta Pruning: The Alpha-Beta Pruning algorithm is a technique used in game trees to reduce the number of nodes that need to be evaluated. It is an enhancement to the minimax algorithm, which is used to determine the best move in games with two players.

## Water Jug Problem Solver

The Water Jug problem solver program allows you to find a solution for measuring a specific amount of water using two jugs with different capacities. It implements a BFS algorithm to explore all possible states and determine if a solution exists.

### Usage

1. Install Python 3 if you haven't already.

2. Run the `water_jug_problem_solver.py` file.

3. Enter the capacities of the two jugs and the target amount of water when prompted.

4. The program will display the steps to measure the target amount of water, or indicate if it is not possible.

## Language Detection

The Language Detection program allows you to detect the language of a given text using the langdetect library in Python. It utilizes the language detection algorithm to analyze the text and determine the most probable language.

### Usage

1. Install Python 3 if you haven't already.

2. Run the `language_detection.py` file.

3. Enter the text for language detection when prompted.

4. The program will display the detected language of the text.

## Alpha-Beta Pruning

The Alpha-Beta Pruning algorithm is a technique used in game trees to reduce the number of nodes that need to be evaluated. It is an enhancement to the minimax algorithm, which is used to determine the best move in games with two players.

### Usage

The `alpha_beta` function in the provided code implements the Alpha-Beta Pruning algorithm. It takes a game tree node, depth, alpha, beta, and a boolean indicating whether it's the maximizing player's turn. The function returns the optimal value of the game tree.

## Dependencies

The Water Jug problem solver program has no external dependencies.

The Language Detection program requires the `langdetect` library. You can install it by running `pip install langdetect`.

The alpha beta pruning solver program has no external dependencies.

## Contributing

Contributions to the Water Jug problem solver and Language Detection programs are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This repository is licensed under the MIT License. Feel free to use and modify the code for your own purposes.
