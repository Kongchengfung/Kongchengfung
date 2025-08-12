import tkinter as tk
from grid import Grid
from search_algorithms import bfs, dfs, gbfs, astar, cus1, cus2

class GridGUI:
    ICONS = {
        'empty': '⬜',
        'wall': '🧱',
        'start': '🤖',
        'goal': '🏁',
        'visited': '🟨',
        'path': '🔵',
    }

    def __init__(self, master, grid_file, algorithm):
        self.grid = Grid(grid_file)
        self.algorithm = algorithm
        self.master = master
        self.labels = [[None for _ in range(self.grid.width)] for _ in range(self.grid.height)]
        self.setup_grid()
        self.run_search()

    def setup_grid(self):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                label = tk.Label(self.master, text=self.ICONS['empty'], font=('Consolas', 36), width=3, height=2)
                label.grid(row=y, column=x)
                self.labels[y][x] = label
                if (x, y) in self.grid.walls:
                    self.set_icon(x, y, 'wall')
                elif (x, y) == self.grid.start:
                    self.set_icon(x, y, 'start')
                elif (x, y) in self.grid.goals:
                    self.set_icon(x, y, 'goal')

    def set_icon(self, x, y, icon_key):
        color_map = {
        'empty': '#e0e0e0',
        'wall': '#444444',
        'start': '#2196F3',   # Blue Gundam
        'goal': '#4CAF50',    # Green base
        'visited': '#FFEB3B', # Yellow radar
        'path': '#03A9F4',    # Blue trail
        }
        
        self.labels[y][x].config(
            text=self.ICONS[icon_key],
            bg=color_map.get(icon_key, 'white'),
            fg='black' if icon_key != 'wall' else 'white'
        )

    def run_search(self):
        search_funcs = {
            'bfs': bfs.search,
            'dfs': dfs.search,
            'gbfs': gbfs.search,
            'astar': astar.search,
            'cus1': cus1.search,  # Placeholder for custom search 1
            'cus2': cus2.search,  # Placeholder for custom search 2
        }

        if self.algorithm not in search_funcs:
            print("Unknown algorithm")
            return

        result = search_funcs[self.algorithm](self.grid)
        if len(result) == 4:
            path, _, _, visited = result

        else:
            path, _, _ = result
            visited = []
    
        self.animate_visited(visited, path)

    def animate_path(self, moves):
        from time import sleep
        self.master.update()
        x, y = self.grid.start

        self.set_icon(x, y, 'empty')
        self.master.update()
        self.master.after(100)

        for move in moves:
            self.set_icon(x, y, 'path')

            if move == 'right':
                x += 1
            elif move == 'down':
                y += 1
            elif move == 'left':
                x -= 1
            elif move == 'up':
                y -= 1

            self.set_icon(x, y, 'start')
            self.master.update()
            self.master.after(200)

    def animate_visited(self, visited, final_path):
        for pos in visited:
            x, y = pos
            if pos == self.grid.start or pos in self.grid.goals:
                continue
            self.set_icon(x, y, 'visited')
            self.master.update()
            self.master.after(50)

        # Animate final path after visited
        if final_path:
            self.animate_path(final_path)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python gui.py <filename> <method>")
        exit(1)

    root = tk.Tk()
    root.title("Robot Navigation with Emojis")
    app = GridGUI(root, sys.argv[1], sys.argv[2].lower())
    root.mainloop()
