import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path

import easyocr
from serial import Serial

from recognize_plates import get_plate_number

def receive_plate_image(serial: Serial) -> np.ndarray:

    # Constants for the small protocol we're using to send the plate images.
    HEIGHT_BYTES = 1 # Sent as a uint8_t
    WIDTH_BYTES = 1 # Sent as a uint8_t
    PLATE_BYTE_COUNT_BYTES = 4 # Sent as a uint32_t

    # 1. Read height and width.
    height_px = int.from_bytes(serial.read(HEIGHT_BYTES))
     
    width_px = int.from_bytes(serial.read(WIDTH_BYTES))
    # 2. Read in the number of bytes comprising the plate image that will be
    #    sent.
    num_bytes = int.from_bytes(serial.read(PLATE_BYTE_COUNT_BYTES))
    # 3. Read as many bytes as instructed in the previous step here.
    plate_image_bytes = serial.read(num_bytes)

    # Now, need to construct the image from the above bytes.
    # Per our small "protocol," the image bytes should be sent starting with the
    # first row and first column, then first row second column, etc. For
    # simplicity, we're assuming that our images are grayscale. So, Grayscale 8
    # bit--meaing we have h rows, w columns, and an 8 bit value (one byte) at
    # each h,w (y,x) position.
    # Starter example: https://stackoverflow.com/a/17170855 and
    # https://stackoverflow.com/a/28235794
    # np.fromstring preferred here, as it makes a copy of the buffer, rather
    # than just creating a view of it (dangerous if the underlying bytes change).
    image_np = np.fromstring(string=plate_image_bytes, dtype=np.int8)
    image = np.reshape(image_np, newshape=(height_px, width_px, 1))
    # image = cv.imdecode(buf=image_np, flags=cv.IMREAD_GRAYSCALE)

    return image

if __name__ == "__main__":
    
    # Open a new serial connection with the specified baud rate and any other
    # parameters.
    print(f"Setting up serial connection.")
    serial_port = ""
    baud_rate = 9600

    print(f"Succes started communication on serial port {serial_port} with baud rate {baud_rate}")

    # Create a new OCR pipeline.
    print("Instantiating new OCR pipeline")
    reader = easyocr.Reader(lang_list=["en"], gpu=False)

    # While true...
    #   receive a new plate
    #   pass the plate through the OCR pipeline.
    #   print out resulting text.

    with Serial(port=serial_port, baudrate=baud_rate) as serial:
        
        while True:
            
            # Read plate image from the serial port.
            plate_image = receive_plate_image(serial=serial)
            # Pass the plate image into the OCR pipeline.
            plate_number = get_plate_number(plate_image=plate_image, reader=reader)
            # Print the plate number.
