import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.Graph()

# Nodo central
centro = "Majo"
G.add_node(centro)

# Tres comunidades
familia = ["Mamá", "Papá", "Hermana", "Abuela"]
barrio = ["Santi", "Sofi", "Juan", "Dani"]
universidad = ["Kevin", "Alejandro", "Laura", "Camilo"]

# Agregar los nodos
G.add_nodes_from(familia)
G.add_nodes_from(barrio)
G.add_nodes_from(universidad)

# Conectar a Majo con todos los integrantes
for persona in familia + barrio + universidad:
    G.add_edge(centro, persona)

# Conexiones de la familia
G.add_edges_from([
    ("Mamá", "Papá"),
    ("Mamá", "Hermana"),
    ("Mamá", "Abuela"),
    ("Papá", "Hermana")
])

# Conexiones de los amigos del barrio
G.add_edges_from([
    ("Santi", "Sofi"),
    ("Santi", "Juan"),
    ("Sofi", "Dani"),
    ("Juan", "Dani")
])

# Conexiones de los compañeros de universidad
G.add_edges_from([
    ("Kevin", "Alejandro"),
    ("Kevin", "Laura"),
    ("Alejandro", "Camilo"),
    ("Laura", "Camilo")
])

# Conexiones entre diferentes comunidades
G.add_edges_from([
    ("Santi", "Kevin"),
    ("Sofi", "Laura"),
    ("Mamá", "Laura")
])

# Posiciones de cada persona
pos = {
    "Majo": (0, 0),

    # Familia
    "Mamá": (-2.8, 2.2),
    "Papá": (-4.0, 1.0),
    "Hermana": (-4.0, 3.0),
    "Abuela": (-2.8, 3.8),

    # Amigos del barrio
    "Santi": (-3.8, -1.2),
    "Sofi": (-2.8, -2.4),
    "Juan": (-4.5, -2.6),
    "Dani": (-1.8, -1.3),

    # Universidad
    "Kevin": (2.8, 2.2),
    "Alejandro": (4.0, 1.0),
    "Laura": (4.0, 3.0),
    "Camilo": (2.8, 3.8)
}

# Tamaño de la ventana
plt.figure(figsize=(13, 9))

# Familia: cuadrados
nx.draw_networkx_nodes(
    G, pos,
    nodelist=familia,
    node_shape="s",
    node_size=1700
)

# Amigos del barrio: círculos
nx.draw_networkx_nodes(
    G, pos,
    nodelist=barrio,
    node_shape="o",
    node_size=1700
)

# Universidad: triángulos
nx.draw_networkx_nodes(
    G, pos,
    nodelist=universidad,
    node_shape="^",
    node_size=1700
)

# Majo: estrella
nx.draw_networkx_nodes(
    G, pos,
    nodelist=[centro],
    node_shape="*",
    node_size=3000
)

# Dibujar conexiones
nx.draw_networkx_edges(
    G, pos,
    width=1.8
)

# Mostrar nombres
nx.draw_networkx_labels(
    G, pos,
    font_size=10,
    font_weight="bold"
)

# Título
plt.title(
    "Red social personal de Majo",
    fontsize=18,
    fontweight="bold"
)

# Leyenda
plt.scatter([], [], marker="s", s=180, label="Familia")
plt.scatter([], [], marker="o", s=180, label="Amigos del barrio")
plt.scatter([], [], marker="^", s=180, label="Compañeros de la universidad")
plt.scatter([], [], marker="*", s=250, label="Majo")

plt.legend(
    loc="lower center",
    bbox_to_anchor=(0.5, -0.03),
    ncol=4
)

# Quitar los ejes
plt.axis("off")
plt.tight_layout()

# Guardar y mostrar el grafo
plt.savefig(
    "red_social_personal_majo.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()