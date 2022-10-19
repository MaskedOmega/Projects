import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

# initialize the WindowCapture class
wincap = WindowCapture('Albion Online Client')

needle_img = cv.imread('Needle.jpg', cv.IMREAD_UNCHANGED)


screenshot=0


threshold = 0.8


loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()

    result = cv.matchTemplate(screenshot, needle_img, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


    if max_val >= threshold:
        print('Found needle.')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]


        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv.rectangle(haystack_img, top_left, bottom_right, 
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)


    else:
        print('Needle not found.')


    cv.imshow('Computer Vision', screenshot)


    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
