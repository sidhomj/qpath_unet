"""

A class for reading Whole-Slide Images and pulling specific frames

Author: @hamelst

"""

import os
import slideio
from pathlib import Path
from typing import Union #TYPE_CHECKING, Iterator, List, Tuple, 
import numpy as np

from functions.utils import flatten

class WSI_reader(object):
    
    def __init__(self, image_path: Union[str, bytes, os.PathLike]=None,
                 image_type: Union[str, bytes, os.PathLike]=None) -> None:
        """
        inputs: 
            - `image_path`: can be string bytes or path object and represents a full or relative image path 
                Ex. "path/to/svs/image.svs"
            - `image_type`: image type according to format from slideio [given here](http://www.slideio.com/drivers.html)
                Ex. "SVS"
        """

        # Make sure image path is given and path is correct
        assert image_path!=None, 'Please make first argument the path to a Whole-Slide Image images'
        self.image_path = Path(image_path)
        self.image_path_str = str(self.image_path)
        assert self.image_path.is_file(), 'Please enter correct path to file. '+str(self.image_path)+' is not actual file'
        
        
        # set correct image tyoe
        self._image_type = image_type
        if self._image_type == None:
            # makes image type an all uppercase version of image_path's extension
            self._image_type = str(os.path.splitext(image_path)[1]).upper()[1:]
            
            
        self.slideio_slide = slideio.open_slide(self.image_path_str, self._image_type)
        self.slideio_scene = self.slideio_slide.get_scene(0)
        # Set default values for arguments
        #    - To-do: add documentation in vein of https://github.com/ysbecca/py-wsi/blob/master/py_wsi/turtle.py
        



    def pull_np(self, coord_tl: Union[tuple, list, np.ndarray]=(0,0), 
                dim: Union[int, float, tuple, list, np.ndarray]=(0,0),
                output_size: Union[int, float, tuple, list, np.ndarray]=(0,0), **kwargs) -> np.ndarray:
        import itertools        
        
        # Work with coordiantes
        #flatten the coordinates list
        if isinstance(coord_tl, np.ndarray):
            coord_tl = tuple(coord_tl.flatten())
        coord_tl = tuple(flatten(coord_tl))
        assert len(coord_tl)==2, "Must have 2-D tuple or list of coordinates–in form (x,y)–from top left origin of image with `length==2`. Leave blank to use (0,0)"
        
        # Work with dimensions
        if isinstance(coord_tl, np.ndarray):
            coord_tl = tuple(coord_tl.flatten())
        if isinstance(dim, int) or isinstance(dim, float):
            dim = (int(dim),int(dim))
        else:
            dim = tuple(flatten(dim))
        assert len(dim)==2, "Must have 2-D tuple or list or array of image dimesnions in form of (width,height) from top left origin of image with `length==2`. Leave blank to pull rest of image"
        
        # Work with output_size
        if isinstance(coord_tl, np.ndarray):
            coord_tl = tuple(coord_tl.flatten())
        if isinstance(output_size, int) or isinstance(output_size, float):
            dim = (int(output_size),int(output_size))
        else:
            dim = tuple(flatten(output_size))
        assert len(output_size)==2, "Must have 2-D tuple or list or array of image dimesnions in form of (width,height) from top left origin of image with `length==2`. Leave blank to pull rest of image"
        
        # combine coordinates and dimensions
        rect = coord_tl+dim
        size = output_size
        
        image = self.slideio_scene.read_block(rect, size, **kwargs)
        
        return(image)
        