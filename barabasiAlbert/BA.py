import networkx as nx
import matplotlib.pylab as plt
import os

n = 410 # number of nodes
m = 3 # number of edges to attach from a new node to existing nodes
graph = nx.generators.random_graphs.barabasi_albert_graph(n, m)

# visualizing the graph
plt.figure(num=None, figsize=(100, 100), dpi=40)
plt.axis('off')
pos = nx.kamada_kawai_layout(graph)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/barabasiAlbert/BA_graph.jpg'))
plt.savefig(figPath)
plt.close()

# plot degree distribution
degrees = [graph.degree(n) for n in graph.nodes()]
degrees = sorted(degrees)
hist = [degrees.count(x) for x in degrees]
plt.plot(degrees, hist, 'o')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('Degree Distribution of BA model')
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/barabasiAlbert/BA_degree_distribution.jpg'))
plt.savefig(figPath)
plt.close()

avgClustering = nx.average_clustering(graph)
density = nx.density(graph)
diameter = nx.diameter(graph)
avgDistance = nx.average_shortest_path_length(graph)
assortativity = nx.degree_assortativity_coefficient(graph)

report = f"""---BA model metrics---
number of nodes: {n}
number of new edges each step: {m}

avg Clustering: {avgClustering:3.3f}
avg Distance: {avgDistance:3.3f}
density: {density:3.3f}
diameter: {diameter}
assortativity: {assortativity:3.3f}"""
f = open("report.txt", "w")
f.write(report)
f.close()