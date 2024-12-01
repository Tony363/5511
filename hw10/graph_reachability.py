from collections import defaultdict

def transpose_graph(graph):
    """
    Transposes the given graph.

    Args:
        graph (dict): The original graph represented as an adjacency list.

    Returns:
        dict: The transposed graph.
    """
    transposed = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def dfs(graph, u, visited, component, marked):
    """
    Performs Depth-First Search (DFS) on the transposed graph, avoiding already marked nodes.

    Args:
        graph (dict): The transposed graph.
        u (int): The current vertex.
        visited (set): Set of visited vertices during this DFS call.
        component (list): List to store the connected component vertices.
        marked (set): Set of all vertices that have been assigned a smallest reachable vertex.
    """
    if u in marked:
        return
    visited.add(u)
    component.append(u)
    for v in graph.get(u, []):
        if v not in visited and v not in marked:
            dfs(graph, v, visited, component, marked)

def find_smallest_reachable_vertices(graph):
    """
    Finds the smallest reachable vertex for each vertex in the graph.

    Args:
        graph (dict): The original graph represented as an adjacency list.

    Returns:
        dict: Mapping from each vertex to the smallest reachable vertex.
    """
    transposed = transpose_graph(graph)
    marked = set()
    result = {}
    for v in sorted(graph.keys()):
        if v not in marked:
            visited = set()
            component = []
            dfs(transposed, v, visited, component, marked)
            for u in component:
                result[u] = v
            marked.update(component)
    return result