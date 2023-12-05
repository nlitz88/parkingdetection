"""Module containing plate reconition prototype pipeline. Note that this
implementation should NOT scaled to run anything more than a demo.
"""

import numpy as np
import cv2 as cv

def dewarp_plate(plate_image: np.ndarray) -> np.ndarray:
    """Applies transforms to the provided image as needed such that the plate in
    the provided image is flat.

    Args:
        plate_image (np.ndarray): The cropped image containing only the license
        plate.

    Returns:
        np.ndarray: The "flattened" image of the license plate.
    """
    pass

def get_plate_number(plate_image: np.ndarray) -> str:
    """Returns the plate number found in the provided image.

    Args:
        plate_image (np.ndarray): The cropped image of the plate in (h,w,c)
        format.

    Returns:
        str: The extracted plate number.
    """

    
    pass