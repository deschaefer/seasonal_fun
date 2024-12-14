# 4882 is too high...


class Node:
    def __init__(self):
        self.x: int
        self.y: int
        self.value = None
        self.visited = False
        self.top: Node = None
        self.right: Node = None
        self.bottom: Node = None
        self.left: Node = None


def f_up(node: Node):
    return node.top


def f_down(node: Node):
    return node.bottom


def f_left(node: Node):
    return node.left


def f_right(node: Node):
    return node.right


f_map = {"^": f_up, "v": f_down, "<": f_left, ">": f_right}


def f_move(node: Node, direction=None):

    if direction:
        target_node = f_map[direction](node)
    else:
        target_node = f_map[node.value](node)

    if target_node:
        if target_node.value == "#":
            return None, target_node.value
        target_node.visited = True
        return target_node, target_node.value
    return None, None


def find_start(root):
    left = root
    right = root

    while left:
        while right:
            if right.value in "^<>v":
                return right
            right = right.right
        left = left.bottom
        right = left


def read_grid():
    grid = []
    row = 0
    with open("data/input_6.txt", "r") as file:
        for line in file:
            line = line.strip()
            grid.append([])
            # each value in the line is distinct, no spaces
            # read each value into a list
            for value in line:
                grid[row].append(value)
            row += 1
    return grid


def build_grid(grid):
    root = None
    prior_row = None
    for y in range(len(grid)):
        prior = None
        x_0 = None
        for x in range(len(grid[y])):
            node = Node()
            if root is None:
                root = node

            if x == 0:
                x_0 = node

            node.x = x
            node.y = y
            node.value = grid[y][x]

            # link left and right
            if prior is not None:
                node.left = prior
                prior.right = node

            if not prior and prior_row:
                node.top = prior_row
                prior_row.bottom = node

            #  link top and bottom
            if prior:
                if prior.top:
                    if prior.top.right:
                        node.top = prior.top.right
                        prior.top.right.bottom = node

            prior = node

        prior_row = x_0

    return root


next_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}


def traverse(root, start_node, direction=None):

    if not direction:
        direction = start_node.value

    start_node.visited = True
    current_node = start_node

    while True:

        next_node, next_value = f_move(current_node, direction)
        # print('------------------')
        # write_grid(root)
        if next_node:
            current_node = next_node
        elif next_value and next_value == "#":
            direction = next_direction[direction]
        elif direction == "v" and not next_value:
            print("good")
            return True
        else:
            direction = next_direction[direction]


def visit_count(node):
    count = 0
    left_node = node
    while left_node:
        while node:
            if node.visited:
                count += 1
            node = node.right
        node = left_node.bottom
        left_node = node

    return count


def write_grid(node):
    count = 0
    left_node = node
    while left_node:
        row = ""
        while node:
            if node.visited:
                row = row + "* "
            else:
                row = row + node.value
            node = node.right
        node = left_node.bottom
        left_node = node
        print(row)

    return count


def main():

    grid = read_grid()
    root = build_grid(grid)
    write_grid(root)

    # find start
    start = find_start(root)
    traverse(root, start)
    print(visit_count(root))


if __name__ == "__main__":
    main()
