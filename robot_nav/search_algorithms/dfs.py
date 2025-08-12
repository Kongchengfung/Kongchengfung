def get_neighbors(pos, grid):
    x, y = pos
    directions = [('right', (x+1, y)), ('down', (x, y+1)), ('left', (x-1, y)), ('up', (x, y-1))]
    return [(move, p) for move, p in directions if grid.is_valid(p)]

def search(grid):
    start = grid.start
    goals = grid.goals
    frontier = [(start, [])]  # stack
    visited = set()
    nodes_expanded = 0
    visit_order = []

    while frontier:
        current, path = frontier.pop()
        if current in visited:
            continue
        visited.add(current)
        visit_order.append(current)
        nodes_expanded += 1
        if current in goals:
            return path, nodes_expanded, current, visit_order

        for move, neighbor in reversed(get_neighbors(current, grid)):  # reversed for correct priority
            if neighbor not in visited:
                frontier.append((neighbor, path + [move]))

    return None, nodes_expanded, None, visit_order
