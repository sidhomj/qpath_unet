from openslide import OpenSlide
from openslide.deepzoom import DeepZoomGenerator
import numpy as np
import matplotlib.pyplot as plt

out = OpenSlide('../H_E/Merad blocks/R1001N_HE.svs')
test = out.get_thumbnail([100,100])
test = np.array(test)
out.dimensions
test = out.read_region((10000,10000),0,(5000,5000))
plt.imshow(test)

zoom_obj = DeepZoomGenerator(out,256,limit_bounds=True)
test = zoom_obj.get_tile(0,[100,100])