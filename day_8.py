def day_8_1():
    import math
    from functools import reduce
    data = './data/day_8.txt'
    with open(data) as file:
        points = [tuple(map(lambda x: int(x), line.rstrip().split(','))) for line in file]

    distances = []
    num_points = len(points)
    num_connections = 1000
    for i in range(num_points):
        point_1 = points[i]
        for j in range(i+1, num_points):
            point_2 = points[j]
            distances.append((point_1, point_2, math.dist(point_1, point_2)))

    distances.sort(key = lambda item: item[2])
    graph = []
    graph_nodes = set()
    for num in range(num_connections):
        graph.append((distances[num][0], distances[num][1]))
        graph_nodes.add(distances[num][0])
        graph_nodes.add(distances[num][1])

    adj_list = {}
    for node in graph_nodes:
        edge_set = set()
        for edge in graph:
            p1, p2 = edge
            if p1 == node:
                edge_set.add(p2)
            if p2 == node:
                edge_set.add(p1)

        adj_list[node] = edge_set

    def nodes_from_bfs(node):
        visited = set()
        q = [node]
        while q:
            n = q.pop()
            visited.add(n)
            neighbors = adj_list[n]
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append(neighbor)

        return visited

    not_visited = graph_nodes.copy()
    connected_components = []
    while not_visited:
        node = not_visited.pop()
        component = nodes_from_bfs(node)
        connected_components.append(component)
        not_visited = not_visited.difference(component)

    connected_components.sort(key = lambda item: -1*len(item))
    return reduce(lambda x, y: x*len(y), connected_components[:3], 1)

def day_8_2():
    import math
    data = './data/day_8.txt'
    with open(data) as file:
        points = [tuple(map(lambda x: int(x), line.rstrip().split(','))) for line in file]

    distances = []
    num_points = len(points)
    num_connections = 1000
    for i in range(num_points):
        point_1 = points[i]
        for j in range(i+1, num_points):
            point_2 = points[j]
            distances.append((point_1, point_2, math.dist(point_1, point_2)))

    distances.sort(key = lambda item: item[2])
    graph = []
    graph_nodes = set()
    for num in range(num_connections):
        graph.append((distances[num][0], distances[num][1]))
        graph_nodes.add(distances[num][0])
        graph_nodes.add(distances[num][1])

    adj_list = {}
    for node in graph_nodes:
        edge_set = set()
        for edge in graph:
            p1, p2 = edge
            if p1 == node:
                edge_set.add(p2)
            if p2 == node:
                edge_set.add(p1)

        adj_list[node] = edge_set

    def nodes_from_bfs(node):
        visited = set()
        q = [node]
        while q:
            n = q.pop()
            visited.add(n)
            neighbors = adj_list[n]
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append(neighbor)

        return visited

    not_visited = graph_nodes.copy()
    connected_components = []
    while not_visited:
        node = not_visited.pop()
        component = nodes_from_bfs(node)
        connected_components.append(component)
        not_visited = not_visited.difference(component)

    for p in set(points):
        if p not in graph_nodes:
            connected_components.append({p})

    while len(connected_components) != 1:
        p1, p2, _ = distances[num_connections]
        p1_comp, p2_comp = None, None
        for i in range(len(connected_components)):
            comp = connected_components[i]
            if p1_comp is None and p1 in comp:
                p1_comp = i
            if p2_comp is None and p2 in comp:
                p2_comp = i
            if p1_comp and p2_comp:
                break
        num_connections+=1
        if p1_comp == p2_comp:
            continue
        elif p1_comp<p2_comp:
            connected_components.append(connected_components[p1_comp].union(connected_components[p2_comp]))
            connected_components.pop(p2_comp)
            connected_components.pop(p1_comp)
        else:
            connected_components.append(connected_components[p1_comp].union(connected_components[p2_comp]))
            connected_components.pop(p1_comp)
            connected_components.pop(p2_comp)
    
    return p1[0]*p2[0]


if __name__ == '__main__':
    print(day_8_1())
    print(day_8_2())
