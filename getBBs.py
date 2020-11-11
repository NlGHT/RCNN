import cv2

# Load all the files with -3
import os
import sys
SOBA_DIR = "./SOBA/SOBA/"
for dirname in os.listdir(SOBA_DIR):
    for image in os.listdir(SOBA_DIR + dirname):
        if image[-6:] == "-3.png":
            print(image)
