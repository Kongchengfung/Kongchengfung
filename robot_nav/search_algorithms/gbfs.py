import heapq

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbors(pos, grid):
    x, y = pos
    directions = [('right', (x+1, y)), ('down', (x, y+1)), ('left', (x-1, y)), ('up', (x, y-1))]
    return [(move, p) for move, p in directions if grid.is_valid(p)]

def search(grid):
    start = grid.start
    goals = grid.goals
    frontier = []
    heapq.heappush(frontier, (0, start, []))
    visited = set()
    nodes_expanded = 0
    visit_order = []

    while frontier:
        _, current, path = heapq.heappop(frontier)
        if current in visited:
            continue
        visited.add(current)
        visit_order.append(current)
        nodes_expanded += 1
        if current in goals:
            return path, nodes_expanded, current, visit_order

        for move, neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                h = min(manhattan(neighbor, goal) for goal in goals)
                heapq.heappush(frontier, (h, neighbor, path + [move]))

    return None, nodes_expanded, None, visit_order
