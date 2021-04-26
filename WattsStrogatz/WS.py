import networkx as nx
import matplotlib.pylab as plt
import os

n = 11 #number of nodes
k = 4 #each node is joined with its k nearest neighbors in a ring topology
p = 0.9 #the probability of rewiring each edge
graph = nx.generators.random_graphs.watts_strogatz_graph(n, k, p)

# visualizing the graph
plt.figure(num=None, figsize=(10, 10), dpi=100)
plt.axis('off')
pos = nx.fruchterman_reingold_layout(graph)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
nx.draw_networkx_labels(graph, pos)
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/WattsStrogatz/WS_graph.jpg'))
plt.savefig(figPath)
plt.close()

# plot degree distribution
degrees = [graph.degree(n) for n in graph.nodes()]
degrees = sorted(degrees)
hist = [degrees.count(x) for x in degrees]
plt.plot(degrees, hist, 'o')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('Degree Distribution of WS model')
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/WattsStrogatz/WS_degree_distribution.jpg'))
plt.savefig(figPath)
plt.close()

avgClustering = nx.average_clustering(graph)
density = nx.density(graph)
diameter = nx.diameter(graph)
avgDistance = nx.average_shortest_path_length(graph)
assortativity = nx.degree_assortativity_coefficient(graph)

report = f"""---WS model metrics---
number of nodes: {n}
number of each node's neighbors in the ring topology: {k}
probability of rewiring each edge: {p}

avg Clustering: {avgClustering:3.3f}
avg Distance: {avgDistance:3.3f}
density: {density:3.3f}
diameter: {diameter}
assortativity: {assortativity:3.3f}"""
f = open("report.txt", "w")
f.write(report)
f.close()