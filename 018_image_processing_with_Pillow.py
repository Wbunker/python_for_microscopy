from PIL import Image
import os

def image_info(image):
    print('Image format:', image.format)
    print('Image mode:', image.mode)
    print('Image size:', image.size)

# img = Image.open('data/0149.tif')
# image_info(img)

img = Image.open('images/test_image.jpg')
image_info(img)

small_img = img.resize((200,300))
small_img.save('images/test_image_small.jpg')

img.thumbnail((200,300))
img.save('images/test_image_thumbnail.jpg')

img = Image.open('images/test_image.jpg')
img_crop = img.crop((0,0,300,300))
img_crop.save('images/test_image_crop.jpg')


img1 = Image.open('images/test_image.jpg')
img2 = Image.open('images/monkey.jpg')
image_info(img2)
img2.thumbnail((150,200))

img1_copy = img1.copy()
img1_copy.paste(img2, (50,50))
img1_copy.save('images/test_image_pasted.jpg')

img_rotate = img1_copy.rotate(45, expand=True)
img_rotate.save('images/test_image_rotate.jpg')

img2 = Image.open('images/monkey.jpg')
img_flipLR = img2.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.save('images/test_image_flipLR.jpg')

grey_img = img2.convert('L')
grey_img.save('images/test_image_grey.jpg')

# iterate over all files in images/test_images/aeroplane folder
# convert each image to grey scale and save it in images/test_images_grey/aeroplane folder
# hint: use os.listdir() to get all files in a folder
# hint: use os.path.join() to join folder name and file name
# hint: use grey_img.save() to save the image
# hint: use grey_img.close() to close the image
# hint: use grey_img = img2.convert('L') to convert image to grey scale
for file in os.listdir('images/test_images/aeroplane'):
    img = Image.open(os.path.join('images/test_images/aeroplane', file))
    grey_img = img.convert('L')
    grey_img.save(os.path.join('images/test_images_grey/aeroplane', file))
    grey_img.close()
    img.close()