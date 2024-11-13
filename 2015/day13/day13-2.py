import networkx as nx
import itertools

with open('input.txt') as f:
    # Graph for determining the best seating arrangement
    G = nx.Graph()

    data = f.read().splitlines()
    for row in data:
        parts = row.split(' ')
        who = parts[0]
        action = parts[2]
        amount = int(parts[3])
        if action == 'lose':
            amount = -amount
        who_with = parts[10][:-1]
        if G.has_edge(who, who_with):
            G[who][who_with]['happiness'] += amount
        else:
            G.add_edge(who, who_with, happiness=amount)

    # Add myself to the graph
    nodes = list(G.nodes)
    for node in nodes:
        G.add_edge('me', node, happiness=0)
        G.add_edge(node, 'me', happiness=0)

    # Find the best seating arrangement
    max_happiness = 0
    for perm in itertools.permutations(G.nodes):
        happiness = 0
        for i in range(len(perm)):
            happiness += G[perm[i]][perm[(i + 1) % len(perm)]]['happiness']
        max_happiness = max(max_happiness, happiness)

    print(max_happiness)
    
