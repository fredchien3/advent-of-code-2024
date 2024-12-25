from itertools import combinations

##### Methods

def has_t_computer(clique):
  for computer in clique:
    if computer[0] == 't': return True
  return False

#####

file = open('input.txt', 'r')
connections = file.read().split('\n')
file.close()

# The list of edges in the graph is also technically a list of
# "2-cliques".
edges = []
for connection in connections:
  c1, c2 = connection.split('-')
  edges.append({c1, c2})

# We can use the "2-cliques" to find "3-cliques".
# Took a lot of searching to find a helpful resource -
# credit where it's due.
# https://iq.opengenus.org/algorithm-to-find-cliques-of-a-given-size-k/

three_cliques = set()
for edge1, edge2 in combinations(edges, 2):
  # XOR - takes the intersection of the pair of edges.
  # If the intersection is an edge (len of 2), and the edge exists in the graph,
  # we have ourselves a 3-clique.
  intersection = edge1 ^ edge2
  if len(intersection) == 2 and intersection in edges:
    three_computers = tuple(sorted(edge1 | edge2))
    three_cliques.add(three_computers)

might_have_historian = [clique for clique in three_cliques if has_t_computer(clique)]

print(len(might_have_historian))