import heapq

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbors(pos, grid):
    x, y = pos
    directions = [('right', (x+1, y)), ('down', (x, y+1)), ('left', (x-1, y)), ('up', (x, y-1))]
    return [(move, p) for move, p in directions if grid.is_valid(p)]

def heuristic(pos, goals):
    h = min(manhattan(pos, goal) for goal in goals)
    return h

def search(grid):
    start = grid.start
    goals = grid.goals
    frontier = []
    heapq.heappush(frontier, (0, 0, start, []))  # (f, g, current, path)
    visited = {}
    nodes_expanded = 0
    visit_order = []

    while frontier:
        f, g, current, path = heapq.heappop(frontier)
        if current in visited and visited[current] <= g:
            continue
        visited[current] = g
        visit_order.append(current)
        nodes_expanded += 1

        if current in goals:
            return path, nodes_expanded, current, visit_order

        for move, neighbor in get_neighbors(current, grid):
            new_g = g + 1
            h = heuristic(neighbor, goals)
            bias = 0
            if move == 'right': bias -= 0.01
            if move == 'down': bias -= 0.005
            heapq.heappush(frontier, (new_g + h + bias, new_g, neighbor, path + [move]))

    return None, nodes_expanded, None, visit_order
