import sys
from grid import Grid
from search_algorithms import bfs, dfs, gbfs, astar, cus1, cus2  # Add more later

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <filename> <method>")
        return

    filename, method = sys.argv[1], sys.argv[2].lower()
    grid = Grid(filename)

    algorithms = {
        'bfs': bfs.search,
        'dfs': dfs.search,
        'gbfs': gbfs.search,
        'astar': astar.search,
        'cus1': cus1.search,  # Placeholder for custom search 1
        'cus2': cus2.search,  # Placeholder for custom search 2
        # Add other methods like dfs, gbfs, as, cus1, cus2
    }

    if method not in algorithms:
        print("Unknown method:", method)
        return

    result = algorithms[method](grid)
    if len(result) == 4:
        path, nodes_expanded, goal, _ = result  # GUI uses this version
    else:
        path, nodes_expanded, goal = result

    print(f"{filename} {method.upper()}")
    print(f"Start at {grid.start}")
    print(f"Goal at {goal if path else 'None'}")
    print(f"{nodes_expanded} nodes expanded")
    print("; ".join(path) if path else "No solution found.")

if __name__ == '__main__':
    main()
