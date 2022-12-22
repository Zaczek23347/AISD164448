from enum import Enum
from typing import Any
from typing import Optional
from typing import Dict, List



class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, vertex: Vertex, list: List[Edge]) -> None:
        self.adjacencies = dict(vertex)



    def create_vertex(self, data: Any) -> Vertex:
        self.adjacencies = {data : []}


    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies


