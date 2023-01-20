"""Contains the class Link"""
from random import random

class Link(object):
    """Represents the weighted link between a node in layer n and layer n+1"""

    def __init__(self, preceding_node_id: tuple, following_node_id: tuple) -> None:
        """Takes tuples representing positions of preceding and following nodes"""
        self.node_before = preceding_node_id
        self.node_after = following_node_id
        self.weight = random() * 2 - 1

    def tweak_weight(self, weight_change: float):
        """Change the weight of the link by weightChange. weight is confined by the interval [-1,1]"""
        self.weight = min(1, max(-1, self.weight + weight_change))
