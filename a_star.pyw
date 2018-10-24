import picture_matrix


class Node(object):
    """cvor pamti svoje koordinate, roditelje(prethodni cvor), vrijednost heuristike"""

    def __init__(self, coordinates, parent, start_dot, goal_dot):
        self.coordinates = coordinates
        self.parent = parent
        self.g = distance(coordinates, start_dot)
        self.h = distance(coordinates, goal_dot)
        self.value = self.g+self.h

    def __str__(self):
        return self.coordinates

    def __hash__(self):
        (x, y) = self.coordinates
        return 1000000 + x * 1000 + y

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def p(self):
        return self.coordinates, self.g, self.h


def distance(dot1, dot2):
    (x1, y1) = dot1
    (x2, y2) = dot2
    return abs(x1 - x2) + abs(y1 - y2)


def get_available_neighbours(node, start_dot, goal_dot, matrix):
    (x, y) = node.coordinates
    neighbours = []
    #  Nije van okvira matrice i nije rep
    if picture_matrix.field_exists((x - 1, y), matrix) and not picture_matrix.is_tail((x - 1, y), matrix):
        t_node = Node((x - 1, y), node, start_dot, goal_dot)
        neighbours.append(t_node)
    if picture_matrix.field_exists((x, y - 1), matrix) and not picture_matrix.is_tail((x, y - 1), matrix):
        t_node = Node((x, y - 1), node, start_dot, goal_dot)
        neighbours.append(t_node)
    if picture_matrix.field_exists((x + 1, y), matrix) and not picture_matrix.is_tail((x + 1, y), matrix):
        t_node = Node((x + 1, y), node, start_dot, goal_dot)
        neighbours.append(t_node)
    if picture_matrix.field_exists((x, y + 1), matrix) and not picture_matrix.is_tail((x, y + 1), matrix):
        t_node = Node((x, y + 1), node, start_dot, goal_dot)
        neighbours.append(t_node)
    return neighbours


# https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
def a_star(matrix):
    start_dot = picture_matrix.find_head(matrix)
    print("start node: ", start_dot)
    goal_dot = picture_matrix.find_apple(matrix)
    print("goal node: ", goal_dot)
    # Initialize open and closed list
    closed_list = []
    opened_list = []

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step

    # Put the start node
    start = Node(start_dot, None, start_dot, goal_dot)
    opened_list.append(start)
    path = []

    # Loop until the goal is reached
    while opened_list:
        # Get current node

        current_node = opened_list.pop(0)
        closed_list.append(current_node)

        # Check if goal is reached
        if current_node.coordinates == goal_dot:
            goal = Node(goal_dot, current_node, start_dot, goal_dot)
            path.append(goal)
            return path

        # Append the neighbours
        neighbours = get_available_neighbours(current_node, start_dot, goal_dot, matrix)
        # Sort the neighbours
        neighbours = sorted(neighbours, key=lambda node: node.h)

        # Loop through neighbours
        for neighbour in neighbours:
            if neighbour in closed_list:
                    continue  # Ignore the neighbor which is already evaluated.(Stay vigilant!)

            # Discover a new node
            if neighbour not in opened_list:
                opened_list.append(neighbour)
            if current_node.h <= neighbour.h:
                continue

            # This path is the best until now. Record it!
            path.append(current_node)
            break
