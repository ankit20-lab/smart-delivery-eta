import random
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edge("Warehouse", "A", weight=random.randint(3,8))

G.add_edge("Warehouse", "B", weight=random.randint(2,6))

G.add_edge("A", "Customer", weight=random.randint(4,10))

G.add_edge("B", "Customer", weight=random.randint(1,5))

G.add_edge("A", "B", weight=random.randint(1,4))

shortest = nx.shortest_path(
    G,
    source="Warehouse",
    target="Customer",
    weight="weight"
)

time = nx.shortest_path_length(
    G,
    source="Warehouse",
    target="Customer",
    weight="weight"
)

print("\nBest Route:")
print(shortest)

print("\nMinimum Delivery Time:")
print(time, "minutes")

centrality = nx.betweenness_centrality(G)

print("Betweenness Centrality:\n")

for node, score in centrality.items():
    print(node, ":", round(score, 3))

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="skyblue",
    font_size=12,
    font_weight="bold",
    arrows=True
)

edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels
)

plt.title("Delivery Network Graph")

plt.show()