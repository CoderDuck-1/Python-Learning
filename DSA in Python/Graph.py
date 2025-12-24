class Graph:
    def __init__(self, edges):
        self.edges = edges #edges is the list containing tuple pairs of related elements
        self.graph_dict ={}
        for value1, value2 in self.edges:
            if value1 not in self.graph_dict:
                self.graph_dict[value1] = [value2]
            else:
                self.graph__dict[value1].append(value2)
            print(self.graph_dict)

    def get_paths(self, start, end, current_path=[]):
        current_path = current_path + [start]
        all_paths=[]
        if start == end:
            return path

        if start not in self.graph_dict:
            return path

        for neighbor in self.graph_dict[start]:
            if neighbor not in current_path:
                possible_paths=self.get_paths(neighbor, end, current_path)
                for each_path in possible_paths:
                    all_paths.append(each_path)

        return all_paths

    def get_shortest_path(self , start, end, current_path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

















