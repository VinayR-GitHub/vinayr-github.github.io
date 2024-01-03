from PIL import Image
import PIL.ImageOps

import os

del_directory = os.listdir('assets/identicons')
for iter_item in del_directory:
    os.remove(f'assets/identicons/{iter_item}')

directory = os.listdir('tools/data')

for iter_item in directory:
    curimg = Image.open(f'tools/data/{iter_item}')
    resimg = PIL.ImageOps.invert(curimg)
    resimg.save(f'assets/identicons/{iter_item}')