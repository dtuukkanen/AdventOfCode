import networkx as nx

# Read the input from input.txt
with open('./2023/day25/input.txt') as f:
    input_data = f.read()

# Create an undirected graph
G = nx.Graph()

# Add edges to the graph
for line in input_data.strip().split('\n'):
    node, neighbors = line.split(': ')
    neighbors = neighbors.split()
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Find the three edges to remove
edges_to_remove = list(nx.edge_betweenness_centrality(G).items())
edges_to_remove.sort(key=lambda x: x[1], reverse=True)
edges_to_remove = [edge for edge, _ in edges_to_remove[:3]]

# Remove the edges
G.remove_edges_from(edges_to_remove)

# Find the connected components
components = list(nx.connected_components(G))
sizes = [len(component) for component in components]

# Multiply the sizes of the two groups
result = sizes[0] * sizes[1]
print(result)