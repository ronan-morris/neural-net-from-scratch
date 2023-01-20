"""Contains the class Layer"""
from node import Node

class Layer(object):
    """Represents a layer of the model"""

    def __init__(self, node_count: int, layer_num: int) -> None:
        """Makes a layer with nodeCount nodes at position layerNum"""
        self.pos_in_model = layer_num
        self.node_ls = list(Node)
        for _ in range(node_count):
            self.node_ls.append(Node())
