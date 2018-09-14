import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

# Create Graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(range(0,9))

# Add edges
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(1, 6)
G.add_edge(6, 4)
G.add_edge(4, 3)
G.add_edge(4, 5)
G.add_edge(6, 7)
G.add_edge(7, 8)
G.add_edge(7, 9)

# Draw graph
#nx.draw(G)
#plt.show()

# Define red and green nodes
red_vertices = [0, 2, 3, 9]
green_vertices = [5, 8]

# Store number of successes
nsuccess = 0

# Execute 1million times this command sequence
for step in range(1, 1000000):
    # Choose a random start node
    vertexid = random.choice([1, 4, 6, 7]) #1
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
