import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float, img_as_ubyte
import scipy.ndimage as ndi
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import exposure
from skimage.segmentation import random_walker

img = img_as_float(io.imread('images/Alloy_noisy.jpg'))

sigma_est = np.mean(estimate_sigma(img, channel_axis=-1))

# slow algorithm
denoise_img = denoise_nl_means( img, 
                            h=1.15 * sigma_est,
                            fast_mode=True,
                            patch_size=5,      # 5x5 patches
                            patch_distance=6)

equalized_img = exposure.equalize_adapthist(denoise_img)

# plt.hist(equalized_img.flat, bins=100, range=(0,1))
# plt.show()

markers = np.zeros(img.shape, dtype=np.uint)
markers[(equalized_img < 0.6) | (equalized_img > 0.3)] = 1
markers[(equalized_img > 0.8) & (equalized_img < 0.99)] = 2

labels = random_walker(equalized_img, markers, beta=10, mode='bf')

segm1 = (labels == 1)
segm2 = (labels == 2)

all_segments = np.zeros((equalized_img.shape[0], equalized_img.shape[1], 3))
all_segments[segm1] = (1,0,0)
all_segments[segm2] = (0,1,0)

plt.imshow(all_segments)
plt.show()