from collections import deque
import class_Map

class BreadthFirstSearch:
    def __init__(self, board, agent, priority):
        self.board = board
        self.agent = agent
        #self.priority = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # Priority order: UP, DOWN, RIGHT, LEFT
        self.priority = priority

    def bfs_search(self, start, goal):
        print("calculation started")
        open_set = deque([start])
        came_from = {}

        while open_set:
            current = open_set.popleft()
            print("Current Node:", current)  # Debug: Print the current node being processed

            if current == goal:
                return self.reconstruct_path(came_from, goal)
            
            for neighbor in self.get_neighbors(current):
                if neighbor not in came_from:
                    open_set.append(neighbor)
                    came_from[neighbor] = current
            
            print("Open Set Length:", len(open_set))  # Debug: Print the length of the open set

        return None


    def is_valid_neighbor(self, neighbor):
                x, y = neighbor
                if 0 <= y < len(self.board.board_data) and 0 <= x < len(self.board.board_data[y]):
                    cell_type = self.board.get_cell_value(neighbor)[0]
                    return cell_type != 0
                return False

    def get_neighbors(self, current):
        neighbors = []
        x, y = current

        for dx, dy in self.priority:
            new_x, new_y = x + dx, y + dy
            new_node = (new_x, new_y)

            if self.is_valid_neighbor(new_node):
                neighbors.append(new_node)

        return neighbors

    def reconstruct_path(self, came_from, goal):
        path = [goal]
        current = goal
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)
        return path

class DepthFirstSearch:
    def __init__(self, board, priority):
        self.board = board
        self.visited = set()
        self.priority = priority
        

    def dfs(self, start, goal):
        stack = deque([start])
        came_from = {}

        while stack:
            current = stack.pop()

            if current == goal:
                path = self.reconstruct_path(came_from, start, goal)
                return path

            if current in self.visited:
                continue

            self.visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    stack.append(neighbor)
                    came_from[neighbor] = current

        return None

    def get_neighbors(self, node):
        x, y = node
         
        neighbors = []

        for dx, dy in self.priority:
            new_x, new_y = x + dx, y + dy
            new_node = (new_x, new_y)

            if self.is_valid_neighbor(new_node):
                neighbors.append(new_node)

        return neighbors

    def is_valid_neighbor(self, neighbor):
            x, y = neighbor
            if 0 <= y < len(self.board.board_data) and 0 <= x < len(self.board.board_data[y]):
                cell_type = self.board.get_cell_value(neighbor)[0]
                return cell_type != 0
            return False
    def reconstruct_path(self, came_from, start, goal):
        path = [goal]
        current = goal
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
