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


def getBBs(filename):
    # Minimum percentage of pixels of same hue to consider dominant colour
    MIN_PIXEL_CNT_PCT = (1.0/10000.0)

    image = cv2.imread(filename)
    if image is None:
        print("Failed to load iamge.")
        exit(-1)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # We're only interested in the hue
    h,_,_ = cv2.split(image_hsv)
    # Let's count the number of occurrences of each hue
    bins = np.bincount(h.flatten())
    print(bins)
    # And then find the dominant hues
    peaks = np.where(bins > (h.size * MIN_PIXEL_CNT_PCT))[0]

    peaks = np.array(peaks)
    print(peaks)

    highLows = [[]]
    # Now let's find the shape matching each dominant hue
    for i, peak in enumerate(peaks):
        # First we create a mask selecting all the pixels of this hue
        peak = np.array(peak)
        mask = cv2.inRange(h, peak, peak)
        xHighest = 0
        xLowest = mask.shape[1]
        yHighest = 0
        yLowest = mask.shape[0]
        if peak != 0:
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
    exit()
    saveCSV(filenameWithoutEnd + ".csv", len(highLows), highLows)
    sys.exit()


# Load all the files with -3
SOBA_DIR = "./SOBA/SOBA/"
for dirname in os.listdir(SOBA_DIR):
    for image in os.listdir(SOBA_DIR + dirname):
        if image[-6:] == "-3.png":
            path = SOBA_DIR + dirname + "/" + image
            getBBs(path)

