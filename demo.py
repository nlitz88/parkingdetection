import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path

import easyocr
from serial import Serial

def receive_plate_image(serial: Serial) -> np.ndarray:

    # Constants for the small protocol we're using to send the plate images.
    HEIGHT_BYTES = 1 # Sent as a uint8_t
    WIDTH_BYTES = 1 # Sent as a uint8_t
    PLATE_BYTE_COUNT_BYTES = 4 # Sent as a uint32_t

    # 1. Read height and width.
    height = serial.read(HEIGHT_BYTES)
    width = serial.read(WIDTH_BYTES)
    # 2. Read in the number of bytes comprising the plate image that will be
    #    sent.
    num_plate_bytes = serial.read(PLATE_BYTE_COUNT_BYTES)
    # 3. Read as many bytes as instructed in the previous step here.
    #

    # However, can't just do this--need to use an iostream of some sort.

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
            
            plate_image = receive_plate_image()