# test iterate over files in a directory
import os
import imageio

directory = os.fsencode('.')
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".jpg"):

		im = imageio.imread(filename)
		im[im < 220] = 0 # this threshold works pretty well, circle is a bit broken with white artifacts near the outside of the circle
		im_out = imageio.imwrite(f'edited_{filename}', im)