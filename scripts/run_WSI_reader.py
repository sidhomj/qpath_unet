import sys
import os
import matplotlib.pyplot as plt
import WSI_reader 

# input
working_directory = '/Users/stevenhamel/Dropbox/My Mac (Steven’s MacBook Pro (2))/Documents/Projects/qpath_unet'
img_path = '/Users/stevenhamel/Dropbox/My Mac (Steven’s MacBook Pro (2))/Documents/Projects/qpath_unet/images/merad_lab_images/R1030/R1030T_HE.svs'


sys.path.append(os.path.join(working_directory,'pkg'))
img_object  =  WSI_reader.WSI_reader(img_path)
svs_np_array = img_object.pull_np((5000,5000),3000,200)

"""WSI_reader.WSI_reader(img_path).pull_np(coords, dimensions, output_size)

        Synopsis
        ----------
        Creates an NP array with a subsection–or the whole image—of a WSI (.svs file) given: coordinates, dimensions (optional), and output size(optional)
        
        Parameters
        ----------
        coordinates: tuple, list, np.ndarray
            Top left coordinates of the subsection to be extracted given in pixels at the highest resolution of the file.
        dim : int, float, tuple, list, np.ndarray
            Dimensions of subsection to be extracted, given in the form of (width,height). If only one number is given
            a square with sides of `dim` length is extracted.
        output_size: int, float, tuple, list, np.ndarray
            size of output, i.e. downsampling or upsampling to have these dimensions

        Returns
        -------
        svs_np_array : np.ndarray
            RGB array of WSI subsection in the format of M*N*3
        """


plt.imshow(svs_np_array)