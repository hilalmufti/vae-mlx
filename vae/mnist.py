import mlx.core as mx
import mlx.nn as nn

class MLP(nn.Module):
    def __init__(self, num_layers, input_dim, hidden_dim, output_dim):
        super().__init__()
        layer_sizes = [input_dim] + [hidden_dim] * num_layers + [output_dim]
        # self.layers = [
        #     nn.Linear(idim, odim) for idim,
        # ]