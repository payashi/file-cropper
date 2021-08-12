import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pydicom

DIR_NAME = 'dir01'
# by dot
UPPER = 80
LOWER = 50
LEFT = 140
RIGHT = 140

dcm_dist = os.path.join(os.path.dirname(__file__), 'dcm')
png_dist = os.path.join(os.path.dirname(__file__), 'png')
npy_dist = os.path.join(os.path.dirname(__file__), 'npy')


def crop_dcm(file: str):
    basename = os.path.basename(file).split('.')[0]

    dcm_out = os.path.join(dcm_dist, f"{basename}.dcm")
    png_out = os.path.join(png_dist, basename)
    npy_out = os.path.join(npy_dist, basename)

    ds = pydicom.dcmread(file)

    ds.PhotometricInterpretation = 'YBR_FULL'

    print(f"{os.path.basename(file)} was encoded as {ds.file_meta.TransferSyntaxUID.name}")
    ds.decompress()

    pixel = ds.pixel_array

    if len(pixel.shape)==3:
        row, col, c = pixel.shape
    else:
        row, col = pixel.shape

    pixel = pixel[UPPER:row-LOWER, LEFT:col-RIGHT]

    ds.PixelData = pixel.tobytes()
    ds.Rows, ds.Columns = pixel.shape[:2]

    ds.save_as(dcm_out)

    plt.imshow(pixel)
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
