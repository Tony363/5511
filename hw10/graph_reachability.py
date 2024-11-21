def dfs(
    u:int, 
    current_label:int,
    label:list,
    GT:list,
)->None:
    label[u] = current_label
    for v in GT[u]:
        if label[v] == 0:
            dfs(v, current_label,label,GT)

def find_smallest_reachable_vertices(
    n:int, 
    edges:list
)->list:
    # Initialize adjacency lists for G^T
    GT = [[] for _ in range(n + 1)]
    for (u, v) in edges:
        GT[v].append(u)  # Reverse the edge direction

    label = [0] * (n + 1)  # Labels for vertices

    for v in range(1, n + 1):
        if label[v] == 0:
            dfs(v, v,label,GT)  # Start DFS with current vertex as label

    return label[1:]  # Exclude index 0 for 1-based indexing


if __name__ == '__main__':
    # Read graph from file
    with open('graph.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]

    print(edges)

    labels = find_smallest_reachable_vertices(n, edges)
    for u in range(1, n + 1):
        print(f"{u}:{labels[u - 1]}")

