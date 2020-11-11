# Standard imports
import cv2
import numpy as np

def detectImage(image):
    # Read image
    im = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 250


    # Filter by Area.
    params.filterByArea = True
    params.minArea = 15
    params.maxArea = 10000

    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.1

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.87

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    params.blobColor = 255

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    print("Hello")

    # Detect blobs.
    keypoints = detector.detect(im)

    print("Hell")

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show blobs
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)


# Load all the files with -3
import os
import sys
SOBA_DIR = "./SOBA/SOBA/"
for dirname in os.listdir(SOBA_DIR):
    for image in os.listdir(SOBA_DIR + dirname):
        if image[-6:] == "-3.png":
            detectImage(image)
            break
