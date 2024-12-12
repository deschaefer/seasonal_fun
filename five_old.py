
class TreeNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        for i, value in enumerate(self.children):
            if value.name == child.name:
                return self.children.pop(i)
        return None

    def find(self, name):
        for i, value in enumerate(self.children):
            if value.name == name:
                return value
        return None

    @staticmethod
    def find_parent(node, name):
        if node.name == name:
            return None
        
        if node.find(name):
            return node
        
        for child in node.children:
            found = TreeNode.find_parent(child, name)
            if found:
                return found
        
        return None


    @staticmethod
    def find_child(node, name):
        
        if node.name == name:
            return node
        
        for child in node.children:
            found = TreeNode.find_child(child, name)
            if found:
                return found
        
        return None

    def __str__(self, level=0):
        ret = " " * (level * 4) + str(self.name) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def read_rules():

    filename = 'data/input_5_a_rules.txt'

    tree = TreeNode('root')

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            left, right = list(line.split('|'))
            left_node = TreeNode.find_child(tree, left)
            right_node = TreeNode.find_child(tree, right)

            if not left_node and not right_node:
                left_node = TreeNode(left)
                tree.add_child(left_node)
                left_node.add_child(TreeNode(right))
            elif left_node and not right_node:
                left_node.add_child(TreeNode(right))
            elif left_node and right_node:
                # need to move nodes around
                parent_node = TreeNode.find_parent(tree, right)
                parent_node.remove_child(right_node)
                left_node.add_child(right_node)

    return tree


def main():
    tree = read_rules()
    print(tree)


if __name__ == '__main__':
    main()
