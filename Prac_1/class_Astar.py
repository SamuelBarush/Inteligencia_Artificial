class AStar:
    def __init__(self, board, agent):
        self.board = board
        self.agent = agent

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
        closed_set = set()
        came_from = {}

        g_score = {tuple(start): float('inf')}  # Convert 'start' to a tuple here
        g_score[tuple(start)] = 0

        f_score = {tuple(start): float('inf')}  # Convert 'start' to a tuple here
        f_score[tuple(start)] = self.heuristic(start, goal)

        while open_set:
            current = min(open_set, key=lambda node: f_score[node])  # Remove tuple() here

            if current == tuple(goal):
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.insert(0, current)
                return path

            open_set.remove(current)
            closed_set.add(current)

            for neighbor in self.get_neighbors(list(current)):
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + self.distance(list(current), neighbor)

                if neighbor not in open_set:
                    open_set.append(neighbor)  # Remove tuple() here
                elif tentative_g_score >= g_score[neighbor]:
                    continue

                came_from[neighbor] = current  # Remove tuple() here
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)

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
