import graphviz

class AStar:
    def __init__(self, board, agent,graphname):
        self.board = board
        self.agent = agent
        self.explored_nodes = set()
        self.paths_to_nodes = {}
        self.graph = graphviz.Digraph(graphname)


    def heuristic(self, node, goal):
        x1, y1 = node
        x2, y2 = goal
        heuristic_cost = abs(x2 - x1) + abs(y2 - y1)
        return heuristic_cost

    def distance(self, node1, node2):
        x1, y1 = node1
        x2, y2 = node2
        cell_type = self.board.get_cell_value(node2)[0]
        agent_costs = self.agent.get_cost_values()
        if cell_type in agent_costs:
            return agent_costs[cell_type] + abs(x2 - x1) + abs(y2 - y1)
        else:
            return float('inf')
    
    def astar_search(self, start, goal):
        open_set = [tuple(start)]
        came_from = {}

        g_score = {tuple(start): 0}
        f_score = {tuple(start): self.heuristic(start, goal)}

        while open_set:
            current = min(open_set, key=lambda node: f_score[node])

            self.graph.node(str(current), label=f'Pos: {current}\n[g: {g_score[current]}, h: {self.heuristic(current, goal)}, f: {g_score[current] + self.heuristic(current, goal)}]')

            if current == tuple(goal):
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.insert(0, current)
                self.paths_to_nodes[tuple(goal)] = path  # Store the path to the goal node
                return path

            open_set.remove(current)
            self.explored_nodes.add(current)

            for neighbor in self.get_neighbors(list(current)):
                if neighbor in self.explored_nodes:
                    continue

                tentative_g_score = g_score[current] + self.distance(list(current), neighbor)

                if neighbor not in open_set:
                    open_set.append(neighbor)
                elif tentative_g_score >= g_score[neighbor]:
                    continue

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)

                # Add an edge to the Graphviz graph to represent the exploration path
                self.graph.edge(str(current), str(neighbor))
        
        
        return None

    def get_neighbors(self, node):
        neighbors = []
        x, y = node

        # Define the possible movements: up, down, left, and right
        movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dx, dy in movements:
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

    def get_explored_nodes(self):
        return list(self.explored_nodes)

    def get_path_to_node(self, node):
        return self.paths_to_nodes.get(tuple(node), [])

    def render_decision_tree(self,graphname):
        print("created")
        return self.graph.render(graphname, view=True, format='pdf', engine='dot')