from collections import deque
import class_Map
import pydot
from PIL import Image

class BreadthFirstSearch:
    def __init__(self, board, agent, priority):
        self.board = board
        self.agent = agent
        self.priority = priority
        self.decisions = {}  # Dictionary to store decisions at each node

    def bfs_search(self, start, goal):
        open_set = deque([start])
        came_from = {}
        self.decisions = {}  # Initialize the decisions dictionary to store neighbor decisions
        
        while open_set:
            current = open_set.popleft()
            #print("Current Node:", current)  # Debug: Print the current node being processed

            if current == goal:
                path, decisions = self.reconstruct_path(came_from, self.board.board_init, goal)
                return path, decisions

            for neighbor in self.get_neighbors(current):
                if neighbor not in came_from:
                    open_set.append(neighbor)
                    came_from[neighbor] = current

                    # Store the decision for the neighbor
                    self.decisions[neighbor] = self.get_decision(current, neighbor)

            #print("Open Set Length:", len(open_set))  # Debug: Print the length of the open set

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

    def reconstruct_path(self, came_from, start, goal):
        path = [goal]
        current = goal
        decisions = []  # List to store decisions

        while current != start:
            current = came_from[current]
            path.append(current)
            decisions.append(self.decisions.get(current, None))  # Get decision from the dictionary

        path.reverse()
        decisions.reverse()
        return path, decisions

    def get_decision(self, current, neighbor):
        current_x, current_y = current
        neighbor_x, neighbor_y = neighbor

        if neighbor_x < current_x:
            return (neighbor, "LEFT")
        elif neighbor_x > current_x:
            return (neighbor, "RIGHT")
        elif neighbor_y < current_y:
            return (neighbor, "UP")
        elif neighbor_y > current_y:
            return (neighbor, "DOWN")
        else:
            return (neighbor, "UNKNOWN")
    def visualize_graph(self, graph_path):
        graph = pydot.Dot(graph_type='graph')

        for node in self.decisions:
            label = f"({node[0]}, {node[1]})\n{self.decisions[node][1]}"
            graph.add_node(pydot.Node(str(node), label=label))

        for node in self.decisions:
            current_x, current_y = node
            for dx, dy in self.priority:
                neighbor_x, neighbor_y = current_x + dx, current_y + dy
                neighbor = (neighbor_x, neighbor_y)

                if neighbor in self.decisions:
                    graph.add_edge(pydot.Edge(str(node), str(neighbor)))

        graph.write(graph_path, format='pdf')
        return graph

class DepthFirstSearch:
    def __init__(self, board, priority):
        self.board = board
        self.visited = set()
        self.priority = priority
        self.decisions = {}
        

    def dfs_search(self, start, goal):
        stack = deque([start])
        came_from = {}
        #decisions = {}  # Create a decisions dictionary to store neighbor decisions

        while stack:
            current = stack.pop()

            if current == goal:
                path = self.reconstruct_path(came_from, start, goal)
                return path, self.decisions

            if current in self.visited:
                continue

            self.visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    stack.append(neighbor)
                    came_from[neighbor] = current

                    # Store the decision for the neighbor
                    self.decisions[neighbor] = self.get_decision(current, neighbor)

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
    
    def get_decision(self, current, neighbor):
        current_x, current_y = current
        neighbor_x, neighbor_y = neighbor

        if neighbor_x < current_x:
            return (neighbor, "LEFT")
        elif neighbor_x > current_x:
            return (neighbor, "RIGHT")
        elif neighbor_y < current_y:
            return (neighbor, "UP")
        elif neighbor_y > current_y:
            return (neighbor, "DOWN")
        else:
            return (neighbor, "UNKNOWN")


    def visualize_graph(self, graph_path):
        graph = pydot.Dot(graph_type='graph')

        for node in self.decisions:
            label = f"({node[0]}, {node[1]})\n{self.decisions[node][1]}"
            graph.add_node(pydot.Node(str(node), label=label))

        for node in self.decisions:
            current_x, current_y = node
            for dx, dy in self.priority:
                neighbor_x, neighbor_y = current_x + dx, current_y + dy
                neighbor = (neighbor_x, neighbor_y)

                if neighbor in self.decisions:
                    graph.add_edge(pydot.Edge(str(node), str(neighbor)))

        graph.write(graph_path, format='pdf')
        return graph