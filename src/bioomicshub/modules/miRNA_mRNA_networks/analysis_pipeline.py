
from __future__ import annotations
import networkx as nx

def centrality_summary(G: nx.Graph) -> dict[str, dict[str, float]]:
    deg = nx.degree_centrality(G)
    btw = nx.betweenness_centrality(G)
    cls = nx.closeness_centrality(G)
    return {"degree": deg, "betweenness": btw, "closeness": cls}
