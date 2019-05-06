import os
from PIL import Image


# Show image
def show_image():
    for image in os.listdir('.'):
        if image.endswith('.jpg'):
            image_to_show = Image.open(image)
            image_to_show.show()


# Change image extension
def change_extension():
    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            image = Image.open(f)
            # Separate filename and extension
            fname, fext = os.path.splitext(f)
            image.save(f'pngs/{fname}.png')


# Resize image with thumbnail to keep aspect ratio
def image_thumbnail():
    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            image = Image.open(f)
            # Separate filename and extension
            fname, fext = os.path.splitext(f)
            output_size = (640, 640)
            image.thumbnail(output_size)
            image.save(f'resize_images/resized_{fname}{fext}')


# Copy an image on top of another image
def logo_on_image():
	image = Image.open('leesin.jpg')
	logo = Image.open('python_logo.png')
	image_copy = image.copy()
	position = ((image_copy.width - logo.width),(image_copy.height-logo.height))
	image_copy.paste(logo,position)
	image_copy.save('leesin_with_logo.jpg')



show_image()
change_extension()
image_thumbnail()
logo_on_image()