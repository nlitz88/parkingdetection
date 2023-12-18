"""Module containing plate reconition prototype pipeline. Note that this
implementation should NOT scaled to run anything more than a demo.
"""

from typing import Optional
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

def get_plate_number(plate_image: np.ndarray,
                     reader: easyocr.Reader,
                     confidence_threshold: Optional[int] = 0.5) -> str:
    """Returns the plate number found in the provided image.

    Args:
        plate_image (np.ndarray): The cropped image of the plate in (h,w,c)
        format, BGR color order.
        reader (easyocr.Reader): The easyocr pipeline that should be used to
        extract the text from the image.

    Returns:
        str: The extracted plate number.
    """
    # Create a new pipeline.
    # TODO This is DEFINITELY not something we should be doing every time we
    # want to extract text from an image--this should be an object that we
    # instantiate during initialization/startup--not at runtime.
    
    
    # Pass the image into the pipeline.
    detections = reader.readtext(image=cv.cvtColor(plate_image, cv.COLOR_BGR2RGB), paragraph=False)
    # print(detections)

    # Sort results by confidence? Filter results for only those that have X or
    # less digits? Or maybe filter by those digits found within the largest box
    # on the plate. Could heuristically filter these out.

    # From the results, because the easyocr reader is also doing text detection,
    # determine which of the detected text regions has the largest area and
    # return the text from that one. We'll assume the largest area contains the
    # license plate number.
    max_area = 0
    max_detection = None
    for i, detection in enumerate(detections):
        prediction_confidence = detection[2]
        if prediction_confidence <= confidence_threshold:
            continue
        # The detected text region corners are the first item in a detection
        # tuple.
        text_corners = detection[0]
        top_left = text_corners[0]
        bottom_right = text_corners[2]
        # Subtract x values to get width, subtract y values to get height.
        width = bottom_right[0] - top_left[0]
        height = bottom_right[1] - top_left[1]
        # Compute area.
        area = height * width
        if area > max_area:
            max_area = area
            max_detection = detection
    
    # Return the text from the max detection if one is found.
    predicted_text = ""
    if max_detection is not None:
        predicted_text = max_detection[1]
        print(f"Returning detected text with confidence above {confidence_threshold} with largest area of {area}")

        # Temporary: Draw results.
        # top_left = tuple(max_detection[0][0])
        # bottom_right = tuple(max_detection[0][2])
        # text = max_detection[1]
        # font = cv.FONT_HERSHEY_SIMPLEX
        # img = cv.rectangle(plate_image,top_left,bottom_right,(0,255,0),3)
        # img = cv.putText(img,text,top_left, font, 0.6,(255,0,0),2,cv.LINE_AA)
        # plt.figure(figsize=(10,10))
        # plt.imshow(img)
        # plt.show()

    else:
        print(f"No text could confidently be extracted.")
    
    return predicted_text

if __name__ == "__main__":
    
    # Load image from file.
    image_filepath = Path(r"C:\Users\nlitz\Desktop\sample_plates\bwbm794.png")
    plate_image = cv.imread(filename=str(image_filepath))

    # Extract license plate number from pipeline.
    reader = easyocr.Reader(lang_list=["en"], gpu=False)
    plate_number = get_plate_number(plate_image=plate_image, reader=reader, confidence_threshold=0.01)
    print(f"Extracted plate number: {plate_number}")
