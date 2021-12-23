# Program created on 12/22/2021 by Uriel Garcilazo Cruz
# Calculate the area of an object in an image using opencv

import os
import cv2
from os.path import join as jn

# Constants
SCALEBAR_COLOR = list(range(180,210))
SCALEBAR_MEAS = 2
SCALEBAR_UNIT = "cm"

# interp. the path to an image in the system

# interp. an image loaded into a CV2 object

# interp. a gray image, transformed using cv2

# interp. a threshold black and white image

# interp. the total number of black pixels in the image 

# interp. number of pixels per unit of measurement, as indicated by scalebar

# interp. no. pixels per square unit



# Calculate area of black shapes in squared SCALEBAR_UNITs

# Total number of black pixels


# If necessary:
# cv2.imshow("test", im1_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()