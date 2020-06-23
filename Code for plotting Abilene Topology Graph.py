import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
G = nx.DiGraph()
a = "ATL_M5"
b = "ATLAng"
c = "CHINng"
d = "DNVRng"
e = "HSTNng"
f = "IPLSng"
g = "KSCYng"
h = "LOSAng"
i = "NYCMng"
j = "SNVAng"
k = "STTLng"
l = "WASHng"

G.add_node(a, pos=(-83.63889, -32.838192))
G.add_node(b, pos=(-84.383300, -33.750000))
G.add_node(c, pos=(-87.616700, -41.833300))
G.add_node(d, pos=(-105.000000, -40.750000))
G.add_node(e, pos=(-95.517364, -29.770031))
G.add_node(f, pos=(-86.159535, -39.780622))
G.add_node(g, pos=(-96.596704, -38.961694))
G.add_node(h, pos=(-118.250000, -34.050000))
G.add_node(i, pos=(-73.966700, -40.783300))
G.add_node(j, pos=(-122.02553, -37.98575))
G.add_node(k, pos=(-122.300000, -47.600000))
G.add_node(l, pos=(-77.026842, -38.897303))

G.add_edge(a, b, weight=(9920000, 1))
G.add_edge(b, a, weight=(9920000, 1))
G.add_edge(b, e, weight=(9920000, 1176))
G.add_edge(b, f, weight=(2480000, 587))
G.add_edge(b, l, weight=(9920000, 846))
G.add_edge(c, f, weight=(9920000, 260))
G.add_edge(c, i, weight=(9920000, 700))
G.add_edge(d, g, weight=(9920000, 639))
G.add_edge(d, j, weight=(9920000, 1295))
G.add_edge(d, k, weight=(9920000, 2095))
G.add_edge(e, b, weight=(9920000, 1176))
G.add_edge(e, g, weight=(9920000, 902))
G.add_edge(e, h, weight=(9920000, 1893))
G.add_edge(f, c, weight=(9920000, 260))
G.add_edge(f, b, weight=(2480000, 587))
G.add_edge(f, g, weight=(9920000, 548))
G.add_edge(g, d, weight=(9920000, 639))
G.add_edge(g, e, weight=(9920000, 902))
G.add_edge(g, f, weight=(9920000, 548))
G.add_edge(h, e, weight=(9920000, 1893))
G.add_edge(h, j, weight=(9920000, 366))
G.add_edge(i, c, weight=(9920000, 700))
G.add_edge(i, l, weight=(9920000, 233))
G.add_edge(j, d, weight=(9920000, 1295))
G.add_edge(j, h, weight=(9920000, 366))
G.add_edge(j, k, weight=(9920000, 861))
G.add_edge(k, d, weight=(992000, 2095))
G.add_edge(k, j, weight=(9920000, 861))
G.add_edge(l, b, weight=(9920000, 896))
G.add_edge(l, i, weight=(9920000, 233))

weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')

nx.draw_networkx(G, pos)
nx.draw_networkx_edge_labels(G, pos, weight)
plt.show()
