from skimage import io
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.filters import sobel, roberts, scharr, prewitt
from skimage.feature import canny
from skimage import restoration

from matplotlib import pyplot as plt
import numpy as np

img = io.imread('images/test_image.jpg', as_gray=True)

rescale_img = rescale(img, 1.0/4.0, anti_aliasing=True)
resize_img = resize(img, (200, 200), anti_aliasing=True)
downscale_img = downscale_local_mean(img, (4, 3))

# plt.figure(figsize=(10,10))
# plt.subplot(2,2,1)
# plt.imshow(img, cmap='gray')
# plt.subplot(2,2,2)
# plt.imshow(rescale_img, cmap='gray')
# plt.subplot(2,2,3)
# plt.imshow(resize_img, cmap='gray')
# plt.subplot(2,2,4)
# plt.imshow(downscale_img, cmap='gray')
# plt.show()

img = io.imread('images/test_image_cropped.jpg', as_gray=True)
edge_roberts = roberts(img)
edge_sobel = sobel(img)
edge_scharr = scharr(img)
edge_prewitt = prewitt(img)

# plt.figure(figsize=(10,10))
# plt.subplot(2,2,1)
# plt.imshow(img, cmap='gray')
# plt.subplot(2,2,2)
# plt.imshow(edge_roberts, cmap='gray')
# plt.subplot(2,2,3)
# plt.imshow(edge_sobel, cmap='gray')
# plt.subplot(2,2,4)
# plt.imshow(edge_scharr, cmap='gray')
# plt.show()

canny_img = canny(img, sigma=2)
# plt.imshow(canny_img, cmap='gray')
# plt.show()

psf = np.ones((3,3)) / 9

deconvolved, _ = restoration.unsupervised_wiener(img, psf)
# plt.imshow(deconvolved, cmap='gray')
# plt.show()

from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import try_all_threshold

img = io.imread('images/scratch.jpg', as_gray=True)
entropy_img = entropy(img, disk(3))
# plt.imshow(entropy_img, cmap='gray')
# plt.show()

# fig, ax = try_all_threshold(entropy_img, figsize=(10,8), verbose=False)
# plt.show()

from skimage.filters import threshold_otsu

thresh = threshold_otsu(entropy_img)
binary = entropy_img <= thresh

# plt.imshow(binary, cmap='gray')
# plt.show()

# find the percentage of pixels that are white
print(np.sum(binary) / binary.size)