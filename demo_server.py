import io
from flask import Flask, request
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

app = Flask(__name__)

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
    numpy_image = np.fromstring(string=jpeg_image_bytes, dtype=np.uint8)
    # print(f"Interpretted numpy array: {numpy_image}")
    # # Decode the JPEG using opencv.
    image = cv.imdecode(buf=numpy_image, flags=cv.IMREAD_COLOR)
    print(f"Decoded image shape: {image.shape}")
    # print(f"CV decoded image: {image}")
    # cv.imshow(winname="Received Image", mat=image)
    # cv.waitKey(10000)
    # preview_image = cv.cvtColor(src=image, code=cv.COLOR_BGR2RGB)
    # plt.imshow(X=preview_image)
    # plt.show()

    # app.logger.info(f"Received new plate image from meter {0}")
    return {
        "plate_number_found": True,
        "plate_number": "ABC1234"
    }

