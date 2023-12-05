"""Module containing plate reconition prototype pipeline. Note that this
implementation should NOT scaled to run anything more than a demo.
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path

import keras_ocr

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
    # Create a new pipeline.
    # TODO This is DEFINITELY not something we should be doing every time we
    # want to extract text from an image--this should be an object that we
    # instantiate during initialization/startup--not at runtime.
    ocr_pipeline =  keras_ocr.pipeline.Pipeline()
    
    # Pass the image into the pipeline.
    predictions = ocr_pipeline.recognize(images=plate_image)

    print(type(predictions))
    print(predictions)
    print(predictions[0])

if __name__ == "__main__":
    
    # Load image from file.
    image_filepath = Path(r"/home/nlitz88/sample_plates/22tv22.png")
    plate_image = cv.imread(filename=image_filepath)

    # Extract license plate number from pipeline.
    plate_number = get_plate_number(plate_image=plate_image)
    print(f"Extracted plate number: {plate_number}")
    