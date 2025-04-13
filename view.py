import networkx as nx
import matplotlib.pyplot as plt
import os

# Create a simple graph for visualization
G = nx.Graph()

# Add nodes
nodes = [0, 1, 2, 3]
G.add_nodes_from(nodes)

# Add edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]  # extra edge to make the graph connected
G.add_edges_from(edges)

# Assume we found the Hamiltonian Path
hamiltonian_path = [0, 1, 2, 3]

# Draw the graph
pos = nx.circular_layout(G)
plt.figure(figsize=(6, 6))

# Draw all edges
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1, alpha=0.5)

# Highlight Hamiltonian path
path_edges = list(zip(hamiltonian_path, hamiltonian_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Draw nodes and labels
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)
nx.draw_networkx_labels(G, pos)

# Title
plt.title("Hamiltonian Path Highlighted in Red")
plt.axis('off')

# Create assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)
# Save the image
plt.savefig("assets/graph.png", format="png")
plt.show()
