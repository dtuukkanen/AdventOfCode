import networkx as nx
from itertools import permutations

with open('input.txt') as f:
    G = nx.Graph()
    data = f.read().splitlines()
    for line in data:
        start = line.split()[0]
        end = line.split()[2]
        distance = int(line.split()[4])
        G.add_edge(start, end, weight=distance)
        G.add_edge(end, start, weight=distance)

# Get all nodes in the graph
nodes = list(G.nodes())

# Initialize the minimum distance to a large value
min_distance = float('inf')

# Iterate over all permutations of nodes to find the shortest path
for perm in permutations(nodes):
    distance = 0
    for i in range(len(perm) - 1):
        distance += G[perm[i]][perm[i + 1]]['weight']
    if distance < min_distance:
        min_distance = distance

print(min_distance)