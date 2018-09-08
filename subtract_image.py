# subtract two images from each other
import os
import imageio
import numpy

directory = os.fsencode('.')
background_image = os.listdir(directory)[0]
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".png"):
		imbackground = imageio.imread(os.fsdecode(background_image))
		im = imageio.imread(filename)
		im = numpy.subtract(im, imbackground)
		im[im < 0] = 0
		im_out = imageio.imwrite(f'subtracted_{filename}', im)