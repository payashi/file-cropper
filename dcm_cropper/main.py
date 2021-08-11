"""
0. install needed packages
    `py -m pip install pydicom matplotlib numpy pylibjpeg` on Windows

1. fetch codes from the remote repository

2. arrange files as below
    dcm_cropper
    |-main.py
    |-dir01
    | |-file01.dcm
    | L-file02.dcm
    |-dir02
    :

3. run the following command
    `python3 main.py`

4. get output folders as below
    dcm_cropper
    |-main.py
    :
    :
    |-png
    ||-file01.png
    |L-file02.png
    |-npy
    ||-file01.npy
    |L-file02.npy
    L-dcm
     |-file01.dcm
     L-file02.dcm
"""

import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pydicom

DIR_NAME = 'dir01'
# by dot
UPPER = 100
LOWER = 0
LEFT = 0
RIGHT = 0

dcm_dist = os.path.join(os.path.dirname(__file__), 'dcm')
png_dist = os.path.join(os.path.dirname(__file__), 'png')
npy_dist = os.path.join(os.path.dirname(__file__), 'npy')


def crop_dcm(file: str):
    basename = os.path.basename(file).split('.')[0]

    dcm_out = os.path.join(dcm_dist, f"{basename}.dcm")
    png_out = os.path.join(png_dist, basename)
    npy_out = os.path.join(npy_dist, basename)

    ds = pydicom.dcmread(file)

    print(f"{os.path.basename(file)} was encoded as {ds.file_meta.TransferSyntaxUID.name}")
    ds.decompress('pylibjpeg')
    pixel = ds.pixel_array

    row, col = pixel.shape
    pixel = pixel[UPPER:row-LOWER, LEFT:col-RIGHT]

    ds.PixelData = pixel.tobytes()
    ds.Rows, ds.Columns = pixel.shape

    ds.save_as(dcm_out)

    plt.imshow(pixel, cmap="gray")
    plt.savefig(png_out)

    np.save(npy_out, pixel)


if __name__ == "__main__":
    os.makedirs(dcm_dist, exist_ok=True)
    os.makedirs(png_dist, exist_ok=True)
    os.makedirs(npy_dist, exist_ok=True)

    files = glob.glob(
        os.path.join(os.path.dirname(__file__), DIR_NAME, "*.dcm")
    )
    for file in sorted(files):
        crop_dcm(file)
        break
