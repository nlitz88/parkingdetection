"""Module containing plate reconition prototype pipeline. Note that this
implementation should NOT scaled to run anything more than a demo.
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path

import easyocr

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
    reader = easyocr.Reader(lang_list=["en"], gpu=False)
    
    # Pass the image into the pipeline.
    result = reader.readtext(image=cv.cvtColor(plate_image, cv.COLOR_BGR2RGB), paragraph=False)
    # predictions = reader.recognize(img_cv_grey=cv.cvtColor(plate_image, cv.COLOR_BGR2GRAY))

    # Temporary: Draw results.
    top_left = tuple(result[0][0][0])
    bottom_right = tuple(result[0][0][2])
    text = result[0][1]
    print(f"Text: {text}")
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.rectangle(plate_image,top_left,bottom_right,(0,255,0),3)
    img = cv.putText(img,text,top_left, font, 0.6,(255,0,0),2,cv.LINE_AA)
    plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.show()

    print(result)
    return result

if __name__ == "__main__":
    
    # Load image from file.
    image_filepath = Path(r"C:\Users\nlitz88\Desktop\sample_plates\n852190.png")
    plate_image = cv.imread(filename=str(image_filepath))

    # Extract license plate number from pipeline.
    plate_number = get_plate_number(plate_image=plate_image)
    print(f"Extracted plate number: {plate_number}")
    