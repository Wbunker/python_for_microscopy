import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernal(size, y_size=None):
    size = int(size)
    if y_size is None:
        y_size = size
    else:
        y_size = int(y_size)
    x, y = np.mgrid[-size:size+1, -y_size:y_size+1]
    g = np.exp(-(x**2/float(size)+y**2/float(y_size)))
    return g / g.sum()

# gaussian_kernal_array = gaussian_kernal(2)
# plt.imshow(gaussian_kernal_array, cmap=plt.get_cmap('jet'), interpolation='nearest')
# plt.colorbar()
# plt.show()


from skimage import io
import scipy.ndimage as ndi
from skimage.restoration import denoise_nl_means, estimate_sigma

img = io.imread('images/denoising/noisy_img.jpg')
gaussian_img = ndi.gaussian_filter(img, sigma=3)

plt.imsave('images/denoising/gaussian.jpg', gaussian_img)


median_img = ndi.median_filter(img, size=3)
plt.imsave('images/denoising/median.jpg', median_img)

sigma_est = np.mean(estimate_sigma(img, channel_axis=-1))

# slow algorithm
denoise = denoise_nl_means( img, 
                            h=1.15 * sigma_est,
                            fast_mode=False,
                            patch_size=5,      # 5x5 patches
                            patch_distance=6,  # 13x13 search area
                            channel_axis=-1)
plt.imsave('images/denoising/nlm.jpg', denoise)