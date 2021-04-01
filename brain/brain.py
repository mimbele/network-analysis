import networkx as nx
import csv
import os
import matplotlib.pylab as plt

#store edges with the right format for networkx to read
brain_edges = open("brain_edges.txt", "a")
for row in csv.reader(open('./brain_edges_verbose.csv', 'r')):
    brain_edges.write(row[0] + ',' + row[1] + '\n')
brain_edges.close()

#read edges
filename = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/brain/brain_edges.txt'))
graph = nx.read_edgelist(filename, delimiter=",", nodetype=str)

# visualize the graph
plt.figure(num=None, figsize=(200, 200), dpi=50)
plt.axis('off')
pos = nx.fruchterman_reingold_layout(graph)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
nx.draw_networkx_labels(graph, pos)
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/brain/brain_graph.jpg'))
plt.savefig(figPath)
plt.close()

# compute assortativity
assortativity = nx.degree_assortativity_coefficient(graph)
print('Assortativity: ' + f"{assortativity:3.2f}")

# compute transitivity
transitivity = nx.transitivity(graph)
print('Transitivity: ' + f"{transitivity:3.2f}")

# compute average shortest path length
average_shortest_path_length = nx.average_shortest_path_length(graph)
print('Average shortest path length: ' + f"{average_shortest_path_length:5.2f}")


## compute centralities ###


## compute degree centrality ##
degree_centrality = nx.degree_centrality(graph) #returns dictionary of nodes with degree centrality as the value
sorted_degree_centrality = sorted(degree_centrality, key=degree_centrality.get, reverse=True)
print('\nTop 5 nodes with highest Degree Centrality: ')
top5nodes = sorted_degree_centrality[0:5]
print( '#1 node ' + top5nodes[0] + ', degree centrality: ' + f"{degree_centrality[top5nodes[0]]:3.2f}"
      + '\n#2 node ' + top5nodes[1] + ', degree centrality: ' + f"{degree_centrality[top5nodes[1]]:3.2f}"
      + '\n#3 node ' + top5nodes[2] + ', degree centrality: ' + f"{degree_centrality[top5nodes[2]]:3.2f}"
      + '\n#4 node ' + top5nodes[3] + ', degree centrality: ' + f"{degree_centrality[top5nodes[3]]:3.2f}"
      + '\n#5 node ' + top5nodes[4] + ', degree centrality: ' + f"{degree_centrality[top5nodes[4]]:3.2f}" )

# plot degree centrality #
x = sorted_degree_centrality
y = []
for i in x:
    y.append(degree_centrality[i])
plt.plot(y, 'o')
plt.title('Degree Centrality (sorted)')
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/brain/brain_degreeCentrality.jpg'))
plt.savefig(figPath)
plt.close()


## compute closeness centrality ##
closeness_centrality = nx.closeness_centrality(graph) #returns dictionary of nodes with closeness centrality as the value
sorted_closeness_centrality = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)
print('\nTop 5 nodes with highest Closeness Centrality: ')
top5nodes = sorted_closeness_centrality[0:5]
print( '#1 node ' + top5nodes[0] + ', closeness centrality: ' + f"{closeness_centrality[top5nodes[0]]:3.2f}"
      + '\n#2 node ' + top5nodes[1] + ', closeness centrality: ' + f"{closeness_centrality[top5nodes[1]]:3.2f}"
      + '\n#3 node ' + top5nodes[2] + ', closeness centrality: ' + f"{closeness_centrality[top5nodes[2]]:3.2f}"
      + '\n#4 node ' + top5nodes[3] + ', closeness centrality: ' + f"{closeness_centrality[top5nodes[3]]:3.2f}"
      + '\n#5 node ' + top5nodes[4] + ', closeness centrality: ' + f"{closeness_centrality[top5nodes[4]]:3.2f}" )

# plot degree centrality #
x = sorted_closeness_centrality
y = []
for i in x:
    y.append(closeness_centrality[i])
plt.plot(y, 'o')
plt.title('Closeness Centrality (sorted)')
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/brain/brain_closenessCentrality.jpg'))
plt.savefig(figPath)
plt.close()


## compute betweenness centrality ##
betweenness_centrality = nx.betweenness_centrality(graph) #returns dictionary of nodes with betweenness centrality as the value
sorted_betweenness_centrality = sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)
print('\nTop 5 nodes with highest Betweenness Centrality: ')
top5nodes = sorted_betweenness_centrality[0:5]
print( '#1 node ' + top5nodes[0] + ', betweenness centrality: ' + f"{betweenness_centrality[top5nodes[0]]:3.2f}"
      + '\n#2 node ' + top5nodes[1] + ', betweenness centrality: ' + f"{betweenness_centrality[top5nodes[1]]:3.2f}"
      + '\n#3 node ' + top5nodes[2] + ', betweenness centrality: ' + f"{betweenness_centrality[top5nodes[2]]:3.2f}"
      + '\n#4 node ' + top5nodes[3] + ', betweenness centrality: ' + f"{betweenness_centrality[top5nodes[3]]:3.2f}"
      + '\n#5 node ' + top5nodes[4] + ', betweenness centrality: ' + f"{betweenness_centrality[top5nodes[4]]:3.2f}" )

# plot betweenness centrality #
x = sorted_betweenness_centrality
y = []
for i in x:
    y.append(betweenness_centrality[i])
plt.plot(y, 'o')
plt.title('Betweenness Centrality (sorted)')
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/brain/brain_betweennessCentrality.jpg'))
plt.savefig(figPath)
plt.close()




## compute pagerank ##
pagerank = nx.pagerank(graph) #returns dictionary of nodes with pagerank as the value
sorted_pagerank = sorted(pagerank, key=pagerank.get, reverse=True)
print('\nTop 5 nodes with highest PageRank: ')
top5nodes = sorted_pagerank[0:5]
print( '#1 node ' + top5nodes[0] + ', pagerank: ' + f"{pagerank[top5nodes[0]]:3.2f}"
      + '\n#2 node ' + top5nodes[1] + ', pagerank: ' + f"{pagerank[top5nodes[1]]:3.2f}"
      + '\n#3 node ' + top5nodes[2] + ', pagerank: ' + f"{pagerank[top5nodes[2]]:3.2f}"
      + '\n#4 node ' + top5nodes[3] + ', pagerank: ' + f"{pagerank[top5nodes[3]]:3.2f}"
      + '\n#5 node ' + top5nodes[4] + ', pagerank: ' + f"{pagerank[top5nodes[4]]:3.2f}" )

# plot pagerank centrality #
x = sorted_pagerank
y = []
for i in x:
    y.append(pagerank[i])
plt.plot(y, 'o')
plt.title('PageRank (sorted)')
figPath = (os.path.join('/home/mimbele/PycharmProjects/pythonProject/brain/brain_pagerank.jpg'))
plt.savefig(figPath)
plt.close()