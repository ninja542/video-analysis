import imageio

im = imageio.imread("C8H18 - Test ID 86000078.jpg")
# im = imageio.imread("imageio:chelsea.png")
new_image_array = [];

# this shows the numbers of the first 10 rows
# the data from the black and white image is different than the color example image
# I think it's because the image is black and white
# time to figure out how to edit image

# trying to eiminate values less than 220:
im[im < 220] = 0 # this threshold works pretty well, circle is a bit broken with white artifacts near the outside of the circle

# writing the new image, will need a way to make it dependent on the initial image name
im_out = imageio.imwrite("edited_image.png", im)