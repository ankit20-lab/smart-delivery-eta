import networkx as nx

G = nx.Graph()

# Roads
G.add_edge("Warehouse", "A", weight=4)
G.add_edge("Warehouse", "B", weight=2)

G.add_edge("A", "Customer", weight=5)
G.add_edge("B", "Customer", weight=3)

# Traffic
traffic = {
    ("B", "Customer"): 10
}

# Apply traffic
for road in traffic:

    u, v = road

    G[u][v]['weight'] += traffic[road]

# Delivery Riders
delivery_riders = {
    "Rider1": "Warehouse",
    "Rider2": "A",
    "Rider3": "B"
}

def assign_best_rider():

    best_rider = None
    best_time = float('inf')

    for rider, location in delivery_riders.items():

        try:

            time = nx.shortest_path_length(
                G,
                location,
                "Customer",
                weight='weight'
            )

            if time < best_time:
                best_time = time
                best_rider = rider

        except:
            pass

    return best_rider, best_time

def get_best_route():

    path = nx.shortest_path(
        G,
        "Warehouse",
        "Customer",
        weight='weight'
    )

    eta = nx.shortest_path_length(
        G,
        "Warehouse",
        "Customer",
        weight='weight'
    )

    rider, rider_eta = assign_best_rider()

    return path, eta, rider, rider_eta