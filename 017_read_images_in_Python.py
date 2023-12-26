from PIL import Image
import numpy as np

img = Image.open('data/0149.tif')
print(type(img))

print(img.format)

img1 = np.asarray(img)
print(type(img1))

##############################################
# Matplotlib
##############################################
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('data/0149.tif')
print(type(img))
print(img.shape)
# plt.imshow(img)
# plt.show()


##############################################
# Scikit-image
##############################################
from skimage import io, img_as_float, img_as_ubyte

img = io.imread('data/0149.tif')
print(type(img))
# plt.imshow(img)
# plt.show()

image_float = img_as_float(img)

##############################################
# OpenCV
##############################################
import cv2

grey_img = cv2.imread('data/0149.tif', 1)
cv2.imshow('image', grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


