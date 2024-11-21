from collections import defaultdict

def transpose_graph(graph):
    transposed = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def dfs(graph, u, visited, component):
    visited.add(u)
    component.append(u)
    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited, component)

def find_smallest_reachable_vertices(graph):
    n = max(graph.keys())
    transposed = transpose_graph(graph)
    marked = set()
    result = {}
    for v in sorted(graph.keys()):
        if v not in marked:
            visited = set()
            component = []
            dfs(transposed, v, visited, component)
            for u in component:
                result[u] = v
            marked.update(component)
    return result

if __name__ == '__main__':
    # Example usage
    graph = {
        1: [2, 4],
        2: [5],
        3: [5, 6],
        4: [2],
        5: [4],
        6: [6]
    }

    result = find_smallest_reachable_vertices(graph)
    for u in sorted(result.keys()):
        print(f"{u}:{result[u]}")
