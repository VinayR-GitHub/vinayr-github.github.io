from PIL import Image
import PIL.ImageOps

import os

directory = os.listdir('tools/colour_invert/data')
print(len(directory))

for iter_item in directory:
    curimg = Image.open(f'tools/colour_invert/data/{iter_item}')
    resimg = PIL.ImageOps.invert(curimg)
    resimg.save(f'assets/identicons/{iter_item}')