"""Contains the Node class"""
from random import random
from link import Link

class Node(object):
    """Represents a node in the network"""

    def __init__(self, min_val:int = 0, max_val:int = 1) -> None:
        """Node initialized with random value on the interval [0,1]"""
        self.min_val, self.max_val = min_val, max_val
        self.value = random() * (max_val - min_val) + min_val
        self.links_forward, self.links_backward = [Link], [Link]

    def reset(self) -> None:
        """Node reinitialized with random value on the interval [0,1] for subsequent runs of the model"""
        self.value = random() * (self.max_val - self.min_val) + self.min_val

    def set_value(self, new_val) -> None:
        """Set the value of the node to newVal"""
        self.value = new_val

    def get_value(self) -> float:
        """Get the current value of the node"""
        return self.value
