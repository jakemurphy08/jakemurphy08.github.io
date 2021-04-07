# Jake Murphy
# April 6, 2021

import glob

# path to the image file
#path = '/Users/jakemurphy/Downloads/Interview Problem/RGB.png'

# opening the image file
#img = open(path,'rb')

#for line in img:
#    print(line)

# path to the image file
imagePath = '/Users/jakemurphy/Downloads/Interview Problem/RGB.png'


for imagePath in glob.glob('/Users/jakemurphy/Downloads/Interview Problem/*.png'):
    image = (imagePath)
    print(imagePath)
