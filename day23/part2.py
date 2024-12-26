from collections import defaultdict

### Modified from https://www.geeksforgeeks.org/maximal-clique-problem-recursive-solution/

def bron_kerbosch(current_clique, potential_nodes, nodes_ruled_out, graph):
  if not potential_nodes and not nodes_ruled_out:
    yield current_clique

  while potential_nodes:
    v = potential_nodes.pop()

    yield from bron_kerbosch(
        current_clique.union({v}),
        potential_nodes.intersection(graph[v]),
        nodes_ruled_out.intersection(graph[v]),
        graph
    )

    nodes_ruled_out.add(v)

###

file = open('input.txt', 'r')
connections = file.read().split('\n')
file.close()

# The list of edges in the graph is also technically a list of
# "2-cliques".
edges = []
for connection in connections:
  c1, c2 = connection.split('-')
  edges.append({c1, c2})

# Create an adjacency list from the edges
graph = defaultdict(set)
for u, v in edges:
  graph[u].add(v)
  graph[v].add(u)

# Convert set keys into sorted lists for consistent ordering
graph = {key: set(graph[key]) for key in graph}

all_cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))

max_clique = sorted(max(all_cliques, key=len))
print(','.join(max_clique))