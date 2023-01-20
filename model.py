"""Contains the class Model"""
from layer import Layer
from link import Link

class Model(object):
    """Represents a network of nodes, each element of shapeArr is the size in nodes of that layer"""
    def __init__(self, shape_arr:list[int]) -> None:
        self.layer_list = [Layer]
        self.num_layers:int = len(shape_arr)
        self.link_map = dict(tuple, Link)
        for i, node_count in enumerate(shape_arr):
            self.layer_list.append(Layer(node_count, i))

    def connect_strongly(self) -> None:
        """For each node in each layer, makes a link """
        for layer_num in range(self.num_layers - 1):
            for front_node_num, front_node in enumerate(self.layer_list[layer_num].node_ls):
                for back_node_num, back_node in enumerate(self.layer_list[layer_num + 1].node_ls):
                    link = Link((layer_num, front_node_num),(layer_num + 1, back_node_num))
                    self.link_map.update((layer_num, front_node_num, back_node_num), link)
                    front_node.links_forward.append(link)
                    back_node.links_backward.append(link)

    def __post_init__(self) -> None:
        self.connect_strongly()
