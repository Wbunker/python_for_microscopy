from scipy import ndimage
from skimage import io, img_as_float, img_as_ubyte
import numpy as np
from matplotlib import pyplot as plt

img = img_as_ubyte(io.imread('images/monkey.jpg', as_gray=False))
print(type(img))
print(img.shape, img.dtype)
print(img.mean(), img.min(), img.max())

flippedLR = np.fliplr(img)
flippedUD = np.flipud(img)

# plat all 3 images in a column
# plt.figure(figsize=(10,10))
# plt.subplot(3,1,1)
# plt.imshow(img)
# plt.subplot(3,1,2)
# plt.imshow(flippedLR)
# plt.subplot(3,1,3)
# plt.imshow(flippedUD)
# plt.show()

rotated = ndimage.rotate(img, 45, reshape=True)
# plt.imshow(rotated, cmap='gray')
# plt.show()

uniform_filter = ndimage.uniform_filter(img, size=3)
# plt.imshow(uniform_filter, cmap='gray')
# plt.show()

gaussian_filter = ndimage.gaussian_filter(img, sigma=2)
# plt.imshow(gaussian_filter, cmap='gray')
# plt.show()

median_filter = ndimage.median_filter(img, size=6)
# plt.imshow(median_filter, cmap='gray')
# plt.show()

sobel_filter = ndimage.sobel(img, axis=0)
plt.imshow(sobel_filter, cmap='gray')
plt.show()