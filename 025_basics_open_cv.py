import cv2

# Read image
img = cv2.imread('images/RGBY.jpg', 1)

print(img.shape)

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

# or you  can do this
blue, green, red = cv2.split(img)

img_merged = cv2.merge((blue, green, red))

# cv2.imshow('Blue pixels', blue)
# cv2.imshow('Green pixels', green)
# cv2.imshow('Red pixels', red)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.imread('images/monkey.jpg', 1)
resized = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)), interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original', img)
cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
