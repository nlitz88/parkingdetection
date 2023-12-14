"""
File: receive_plate_uart.py
Author: Nathan Litzinger (nlitz88@gmail.com)
Description: Contains code to receive image crops of license plates sent to
hub via UART.
"""

import numpy as np
from dataclasses import dataclass

import serial

@dataclass
class PlateImageMetadata:
    """Container for the metadata that will be received from meter with each
    plate that is transmitted.
    """
    num_bytes: int
    plate_height_px: int
    plate_width_px: int
    # NOTE: May eventually need to add number of channels in image, as RGB
    # images may be needed for better OCR performance downstream.

def read_plate_uart(uart_connection: serial.Serial) -> np.ndarray:

    # Read one byte for the height.

    # Read one byte for the width.

    # Read 4 bytes to get the number of bytes (n) in the transmitted plate
    # image.

    # Read the n bytes of the plate image.

    # Reorganize bytes to be an image in H,W,C format (whatever the opencv
    # standard is). NOTE that the image will be in grayscale for now.

    # Return the numpy array.
    pass

# I.e., read in height, then width (two bytes each)
# then num_bytes, then 