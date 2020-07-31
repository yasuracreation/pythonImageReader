import os
import sys
from PIL import Image

imageFolder = sys.argv[1]
output_directory = sys.argv[2]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for fileName in os.listdir(imageFolder):
    clean_name = os.path.splitext(fileName)[0]
    img = Image.open(f'{imageFolder}{fileName}')
    img.save(f'{output_directory}{clean_name}.png', 'png')
    print("saved")
