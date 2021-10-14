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

plt.imshow(svs_np_array)