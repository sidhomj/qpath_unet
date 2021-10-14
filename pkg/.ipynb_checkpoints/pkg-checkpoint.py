import tensorflow as tf
import numpy as np
import os
from pkg.functions import Layers

class pkg(object):
    def __init__(self, name='model_name'):
        self.name = name
        directory = self.name
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _build(self):
        encoder = Layers.encoder()
        bottleneck = Layers.bottleneck(encoder.outputs[0].shape[1:])
        conv_dims = []
        for _ in encoder.outputs[1:]:
            conv_dims.append(list(_.shape[1:]))
        decoder = Layers.decoder(list(bottleneck.outputs[0].shape[1:]),conv_dims,output_dim=[256,256],output_channels=2)

