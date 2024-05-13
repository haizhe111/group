from .i3d import i3d
model_zoo = {
    'i3d': i3d,
}

def BackboneBuilder(config):
    model = model_zoo[config.type](config)
    return model
