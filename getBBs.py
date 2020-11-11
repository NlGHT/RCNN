import os
import sys
import csv
import cv2
import numpy as np

def saveCSV(filename, rois, rows):
    # writing to csv file
    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(str(rois))

        csvwriter.writerows(rows)


def countColours(filename):
    colours = []
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    if image is None:
        print("Failed to load iamge.")
        exit(-1)

    r,g,b = cv2.split(image)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            valR = r[y, x]
            valG = g[y, x]
            valB = b[y, x]
            if valR > 0 or valG > 0 or valB > 0:
                testColour = (float(valR), float(valG), float(valB))
                if testColour not in colours:
                    colours.append(testColour)

    return colours


def getBBs(filename, colours):
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    if image is None:
        print("Failed to load iamge.")
        exit(-1)

    highLows = []
    # Now let's find the shape matching each dominant hue
    for i in range(len(colours)):
        colour = colours[i]
        # First we create a mask selecting all the pixels of this hue
        print(colour)
        mask = cv2.inRange(image, colour, colour)
        xHighest = 0
        xLowest = mask.shape[1]
        yHighest = 0
        yLowest = mask.shape[0]
        for y in range(mask.shape[0]):
            for x in range(mask.shape[1]):
                if mask[y, x] == 255:
                    xHighest = np.maximum(xHighest, x)
                    xLowest  = np.minimum(xLowest, x)
                    yHighest = np.maximum(yHighest, y)
                    yLowest  = np.minimum(yLowest, y)

        highLows.append([xLowest, yLowest, xHighest, yHighest])

    filenameWithoutEnd = filename[:-6]
    print(filenameWithoutEnd)
    print(highLows)
    print(len(highLows))
    saveCSV(filenameWithoutEnd + ".csv", len(highLows), highLows)
    sys.exit()


# Load all the files with -3
SOBA_DIR = "./SOBA/SOBA/"
for dirname in os.listdir(SOBA_DIR):
    for image in os.listdir(SOBA_DIR + dirname):
        if image[-6:] == "-3.png":
            path = SOBA_DIR + dirname + "/" + image
            colours = countColours(path)
            print(colours)
            getBBs(path, colours)

