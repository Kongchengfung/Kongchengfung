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
    heapq.heappush(frontier, (0, 0, start, []))  # (f, g, current_pos, path)
    visited = dict()  # maps position -> best g(n)
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
            h = min(manhattan(neighbor, goal) for goal in goals)
            new_f = new_g + h
            heapq.heappush(frontier, (new_f, new_g, neighbor, path + [move]))

    return None, nodes_expanded, None, visit_order
