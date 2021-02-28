import math
from typing import List
from layer import Layer
from functools import reduce, total_ordering

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def d_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

class Model:
    def __init__(self) -> None:
        self.layers = []

    def addLayer(self, neurons: int, input_shape: int = None) -> None:
        if not self.layers:
            if not input_shape:
                raise Exception('Input shape not defined on first layer')
            self.layers.append( Layer(input_shape, neurons ))
        else:
            # Sets the input shape neurons from last layer
            self.layers.append( Layer(self.layers[-1].neurons, neurons ))
    
    def local_cost(self, output_activations: List[float], expected_activations: List[float]):
        assert len(output_activations) == len(expected_activations)
        
        loss = 0
        for predicted, expected in zip(output_activations, expected_activations):
            loss += pow(predicted-expected, 2)

        return loss
    
    def predict(self, inputs: List[float]) -> List[float]:
        # There are layers that exist
        assert(self.layers) 
        # The first layer accepts input shape
        assert(self.layers[0].num_weights == len(inputs))

        for layer in self.layers:
            inputs = layer.get_activations(inputs, sigmoid)

        return inputs

if __name__ == "__main__":
    pass