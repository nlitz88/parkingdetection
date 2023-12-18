"""Module containing a rough demo flask server to demo the end to end parking
detection system.
"""
import io
from os import PathLike

import numpy as np
import cv2 as cv
from flask import Flask, request
import matplotlib.pyplot as plt
import easyocr

from recognize_plates import get_plate_number

class DemoApp(Flask):
    def __init__(self, import_name: str, static_url_path: str | None = None, static_folder: str | PathLike | None = "static", static_host: str | None = None, host_matching: bool = False, subdomain_matching: bool = False, template_folder: str | PathLike | None = "templates", instance_path: str | None = None, instance_relative_config: bool = False, root_path: str | None = None):
        super().__init__(import_name, static_url_path, static_folder, static_host, host_matching, subdomain_matching, template_folder, instance_path, instance_relative_config, root_path)
        # Initialize the OCR pipeline here before handling any requests--that
        # way we don't have to load the pipeline each time we handle a request.
        # Extract license plate number from pipeline. NOTE That long term, would
        # need to make sure the reader is synchronized.
        self.reader = easyocr.Reader(lang_list=["en"], gpu=False)

app = DemoApp(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/process_plate", methods=["POST"])
def process_plate():
    # Make sure the image being sent is encoded as a JPEG.
    if request.content_type != "image/jpeg" and request.content_type != "image/png":
        app.logger.error(f"Image type was not JPEG or PNG, received content type {request.content_type} instead!")
        return (f"Data with unsupported content type {request.content_type} received. Only image/jpeg and image/png are supported!", 415)
    # Get the JPEG encoded image data from the request as a byte array.
    jpeg_image_bytes = request.get_data(cache=True, as_text=False, parse_form_data=False)
    # Create a numpy array from the byte array.
    numpy_image = np.frombuffer(buffer=jpeg_image_bytes, dtype=np.uint8)
    # Decode the JPEG using opencv. The height and width of the image are
    # encoded as a part of the JPEG byte stream.
    image = cv.imdecode(buf=numpy_image, flags=cv.IMREAD_COLOR)
    # Feed the image into the OCR pipeline to attempt to extract the plate
    # number.
    plate_number = get_plate_number(plate_image=image, reader=app.reader)
    # Build response based on pipeline output.
    if plate_number == "":
        app.logger.warning("Failed to confidently identify license plate number in plate image!")
        return {
            "plate_number_found": False,
            "plate_number": ""
        }
    else:
        return {
            "plate_number_found": True,
            "plate_number": plate_number
        }

if __name__ == "__main__":
    # Run the app if the file is invoked directly.
    app.run(host="0.0.0.0", port=5000, debug=True)