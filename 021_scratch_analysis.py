from skimage.filters.rank import entropy
from skimage.filters import threshold_otsu
from skimage.morphology import disk
from skimage import io
from matplotlib import pyplot as plt
import numpy as np

img = io.imread('images/scratch.jpg', as_gray=True)
entropy_img = entropy(img, disk(10))
thresh = threshold_otsu(entropy_img)

binary = entropy_img <= thresh

# print the percentage of the image that is scratched
print(np.sum(binary) / binary.size)


# loop over the scratch images in images/scratch_assay folder and plot the percentage of the image that is scratched
import glob
path = 'images/scratch_assay/*.*'
percentage_scratched = []
for filename in sorted([filename for filename in glob.glob(path) ]  ):
    print(filename)
    img = io.imread( filename, as_gray=True)
    entropy_img = entropy(img, disk(10))
    thresh = threshold_otsu(entropy_img)
    binary = entropy_img <= thresh
    percentage_scratched.append(np.sum(binary))

# plt.plot(range(0,len(percentage_scratched)), percentage_scratched)
# plt.show()

from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(range(0,len(percentage_scratched)), percentage_scratched)
print(slope, intercept, r_value, p_value, std_err)
