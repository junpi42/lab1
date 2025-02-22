from Search import Search


class DepthFirst(Search):
    def __init__(self, problem):
        Search.__init__(self, problem)
        self.openNodes = []

    def insert_node(self, new_node, node_list):
        node_list.append(new_node)

    def extract_node(self, node_list):
        return node_list.pop()

    def is_empty(self, node_list):
        if not self.open_list:
            return False
        return True
