import random
from folium.plugins import AntPath
import folium

# Kolkata location


m = folium.Map(location=[22.5826, 88.3739], zoom_start=12)
eta = random.randint(8, 20)

traffic_status = random.choice([
    "Low",
    "Moderate",
    "Heavy"
])
print("ETA:", eta)
print("Traffic:", traffic_status)

rider_lat = 22.5840 + random.uniform(-0.003, 0.003)
rider_lon = 88.3750 + random.uniform(-0.003, 0.003)

eta_html = f"""
<div style="
position: fixed;
top: 20px;
right: 20px;
width: 260px;
height: 180px;
background-color: white;
z-index:9999;
font-size:16px;
border-radius:10px;
padding:15px;
box-shadow: 2px 2px 10px gray;
">

<h4>🚚 Live Delivery ETA</h4>

<b>Status:</b> On Route <br>

<b>ETA:</b> {eta} Minutes <br>

<b>Traffic:</b> {traffic_status} 🚦

<br>
<b>Rider Lat:</b> {rider_lat:.4f} <br>
<b>Rider Lon:</b> {rider_lon:.4f}
</div>
"""

from branca.element import Element

m.get_root().html.add_child(Element(eta_html))

# Warehouse

folium.CircleMarker(

    location=[22.5726, 88.3639],

    radius=15,

    popup="🏭 MAIN WAREHOUSE",

    tooltip="🏭 Warehouse",

    color="black",

    fill=True,

    fill_color="yellow",

    fill_opacity=1

).add_to(m)

# Hub A
# Delivery Rider


folium.Marker(
    [22.5826, 88.3739],
    popup="Hub A",
    icon=folium.Icon(color="red")
).add_to(m)

# Customer
folium.Marker(
    [22.5926, 88.3839],
    popup="Customer",
    icon=folium.Icon(color="green")
).add_to(m)

# Route line
best_route = [
    [22.5726, 88.3639],  # Warehouse
    [22.5826, 88.3739],  # Hub A
    [22.5926, 88.3839]   # Customer
]
rider_locations = [

    [22.5726, 88.3639],

    [22.5750, 88.3660],

    [22.5780, 88.3690],

    [22.5810, 88.3720],

    [22.5840, 88.3750],

    [22.5870, 88.3780],

    [22.5900, 88.3810]

]
current_position = random.choice(rider_locations)

rider1 = [
    [22.5650, 88.3550],
    [22.5826, 88.3739]
]

rider2 = [
    [22.5626, 88.3539],
    [22.5726, 88.3639]
]

rider3 = [
    [22.5926, 88.3839],
    [22.6026, 88.3939]
]

folium.Marker(
    rider1[-1],

    popup="🚚 Rider 1",

    icon=folium.Icon(color="blue")
).add_to(m)

folium.Marker(
    rider2[-1],

    popup="🚚 Rider 2",

    icon=folium.Icon(color="green")
).add_to(m)

folium.Marker(
    rider3[-1],

    popup="🚚 Rider 3",

    icon=folium.Icon(color="red")
).add_to(m)





folium.Marker(

    current_position,

    popup="🚚 Delivery Rider",

    tooltip="Live Rider",

    icon=folium.Icon(
        color="orange",
        icon="truck",
        prefix="fa"
    )
).add_to(m)

AntPath(
    best_route,
    color="blue",
    weight=6,
    delay=800
).add_to(m)

AntPath(
    rider1,
    color="blue"
).add_to(m)

AntPath(
    rider2,
    color="green"
).add_to(m)

AntPath(
    rider3,
    color="red"
).add_to(m)

# Traffic zone
folium.Circle(
    location=[22.5826, 88.3739],
    radius=500,
    color="red",
    fill=True,
    fill_opacity=0.4,
    popup="Heavy Traffic Area"
).add_to(m)

AntPath(
    locations=[
        [22.5726, 88.3639],
        [22.5826, 88.3739],
        [22.5926, 88.3839]
    ],
    color="blue",
    weight=6,
    delay=800
).add_to(m)

m.save("delivery_map.html")

print("Map created successfully!")