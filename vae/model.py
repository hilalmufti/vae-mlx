import mlx.core as mx
import mlx.nn as nn

class MLP(nn.Module):
    def __init__(self, num_layers, input_dim, hidden_dim, output_dim):
        super().__init__()
        ss = [input_dim] + [hidden_dim] * num_layers + [output_dim] # sizes
        self.ls = [
            nn.Linear(i, o) for i, o in zip(ss[:-1], ss[1:]) # layers
        ]

    # def __call__(self, x):