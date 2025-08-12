from collections import deque

def spiral_directions():
    # Clockwise direction rotation
    return [
        ('right', (1, 0)),
        ('down', (0, 1)),
        ('left', (-1, 0)),
        ('up', (0, -1))
    ]

def get_neighbors(pos, grid, offset=0):
    x, y = pos
    directions = spiral_directions()
    # Rotate directions based on layer offset to simulate spiral progression
    directions = directions[offset % 4:] + directions[:offset % 4]
    return [(move, (x + dx, y + dy)) for move, (dx, dy) in directions if grid.is_valid((x + dx, y + dy))]

def search(grid):
    start = grid.start
    goals = grid.goals
    frontier = deque([(start, [], 0)])  # (position, path, spiral offset)
    visited = set()
    nodes_expanded = 0
    visit_order = []

    while frontier:
        current, path, layer = frontier.popleft()
        if current in visited:
            continue
        visited.add(current)
        visit_order.append(current)
        nodes_expanded += 1

        if current in goals:
            return path, nodes_expanded, current, visit_order

        for move, neighbor in get_neighbors(current, grid, offset=layer):
            if neighbor not in visited:
                frontier.append((neighbor, path + [move], layer + 1))

    return None, nodes_expanded, None, visit_order  
