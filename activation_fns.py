"""Contains various activation functions
(determine what value a node should take based on its input)"""
from math import tanh, exp

def linear(input: float):
    """Returns the input"""
    return input

def binary(input: float, threshold: float):
    """returns -1 or 1"""
    return int(input > threshold) * 2 - 1

def tanh(input: float):
    """domain (-∞, ∞) range (-1, 1)"""
    return tanh(input)

def exponentiate(input: float):
    """domain (-∞, ∞) range (0, ∞)"""
    return exp(input)

def sigmoid(input: float):
    """domain (-∞, ∞) range (0, 1)"""
    return 1 / (1 + exp(-input))