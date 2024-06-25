import os
import imageio.v3 as iio

directory = "images"

filenames = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.png')]

images = [iio.imread(filename) for filename in filenames]

iio.imwrite('team.gif', images, duration = 500, loop = 0)