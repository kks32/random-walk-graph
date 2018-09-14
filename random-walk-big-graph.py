import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

# Create Graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(range(0,27))

# Add edges
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(1, 5)
G.add_edge(4, 5)
G.add_edge(3, 4)
G.add_edge(4, 10)
G.add_edge(9, 10)
G.add_edge(8, 9)
G.add_edge(9, 17)
G.add_edge(17, 16)
G.add_edge(15, 16)
G.add_edge(24, 16)
G.add_edge(17, 18)
G.add_edge(18, 25)
G.add_edge(18, 19)
G.add_edge(11, 19)
G.add_edge(10, 11)
G.add_edge(20, 19)
G.add_edge(20, 26)
G.add_edge(20, 21)
G.add_edge(21, 22)
G.add_edge(22, 27)
G.add_edge(22, 23)
G.add_edge(21, 13)
G.add_edge(11, 12)
G.add_edge(12, 13)
G.add_edge(14, 13)
G.add_edge(12, 6)
G.add_edge(7, 6)
G.add_edge(5, 6)

# Draw graph
#nx.draw(G)
#plt.show()

# Define red and green nodes
red_vertices = [0, 3, 8, 15, 2, 7, 14, 23]
green_vertices = [24, 25, 26, 27]

# Store number of successes
nsuccess = 0

# Execute 10million times this command sequence
for step in range(1, 10000000):
    # Choose a random start node
    vertexid = 1
    # Dictionary that associate nodes with the amount of times it was visited
    visited_vertices = {}
    # Store and print path
    path = [vertexid]
    
    print("Step: %d" % (step))
    # Restart the cycle
    counter = 0
    # Execute the random walk with size 100,000 (100,000 steps)
    for counter in range(1, 100000): 
        # Extract vertex neighbours vertex neighborhood
        vertex_neighbors = [n for n in G.neighbors(vertexid)]
        # Set probability of going to a neighbour is uniform
        probability = []
        probability = probability + [1./len(vertex_neighbors)] * len(vertex_neighbors)
        # Choose a vertex from the vertex neighborhood to start the next random walk
        vertexid = np.random.choice(vertex_neighbors, p=probability)
        # Accumulate the amount of times each vertex is visited
        if vertexid in visited_vertices:
            visited_vertices[vertexid] += 1
        else:
            visited_vertices[vertexid] = 1

        # Append to path
        path.append(vertexid)
        
        # If reached red break
        if vertexid in red_vertices:
            break;
        # If reached green break
        if vertexid in green_vertices:
            nsuccess = nsuccess + 1
            break;

    # Organize the vertex list in most visited decrescent order
    mostvisited = sorted(visited_vertices, key = visited_vertices.get,reverse = True)
    print("Path: ", path)
    # Separate the top 10 most visited vertex
    print("Most visited nodes: ", mostvisited[:10])

print ("# of success: %d of %d" % (nsuccess, step))
print ("Probability of reaching green : %.12f" % (nsuccess / step))
