import snap
import networkx as nx
import matplotlib.pylab as plt

n = 1015 # number of nodes
p1 = 0.44 # Forward probability of an edge
p2 = 0.33 # backward probability of an edge.

snap.GenForestFire(n , p1, p2).SaveEdgeList('edgelist.txt')


with open('./edgelist.txt') as f:
    graph = nx.read_edgelist(f)

# visualizing the graph
plt.figure(num=None, figsize=(100, 100), dpi=40)
plt.axis('off')
pos = nx.kamada_kawai_layout(graph)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
figPath = '/home/mimbele/PycharmProjects/pythonProject/ForestFire/FF_graph.jpg'
plt.savefig(figPath)
plt.close()


# plot degree distribution
degrees = [graph.degree(n) for n in graph.nodes()]
degrees = sorted(degrees)
hist = [degrees.count(x) for x in degrees]
plt.plot(degrees, hist, 'o')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('Degree Distribution of FF model')
figPath = '/home/mimbele/PycharmProjects/pythonProject/ForestFire/FF_degree_distribution.jpg'
plt.savefig(figPath)
plt.close()

avgClustering = nx.average_clustering(graph)
density = nx.density(graph)
diameter = nx.diameter(graph)
avgDistance = nx.average_shortest_path_length(graph)
assortativity = nx.degree_assortativity_coefficient(graph)

report = f"""---FF model metrics---
number of nodes: {n}
forward burn probability: {p1}
backward burn probability: {p2}

avg Clustering: {avgClustering:3.3f}
avg Distance: {avgDistance:3.3f}
density: {density:3.3f}
diameter: {diameter}
assortativity: {assortativity:3.3f}"""
f = open("report.txt", "w")
f.write(report)
f.close()