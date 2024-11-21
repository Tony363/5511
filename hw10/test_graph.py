from collections import defaultdict
from graph_reachability import find_smallest_reachable_vertices

def load_graph_from_file(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as file:
        lines = file.readlines()
        nodes_line = next((line for line in lines if line.startswith('Nodes')), None)
        edges_index = lines.index('Edges:\n')
        nodes = nodes_line.strip().split(':')[1].split(',')
        nodes = [int(node.strip()) for node in nodes]
        for node in nodes:
            graph[node]  # Ensure all nodes are in the graph
        for line in lines[edges_index+1:]:
            if line.strip():
                u_str, v_str = line.strip().split('->')
                u = int(u_str.strip())
                v = int(v_str.strip())
                graph[u].append(v)
    return graph

if __name__ == '__main__':
    # List of test files
    test_files = [
        'tests/disconnected_graph.txt', 
        'tests/self_loops.txt', 
        'tests/complete_graph.txt', 
        'tests/graph_cycles.txt', 
        'tests/single_vertex.txt'
    ]

    for test_file in test_files:
        print(f"\nTesting with {test_file}:")
        graph = load_graph_from_file(test_file)
        result = find_smallest_reachable_vertices(graph)
        for u in sorted(result.keys()):
            print(f"{u}:{result[u]}")
