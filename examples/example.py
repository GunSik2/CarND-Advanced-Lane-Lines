import cv2
import numpy as np

def warper(img, src, dst):

    # Compute and apply perpective transform
    img_size = (img.shape[1], img.shape[0])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_NEAREST)  # keep same size as input image

    return warped

def histogram():
    binary_warped= np.array([[1, 2, 3], [1, 2, 3]])
    print(binary_warped)

histogram()
