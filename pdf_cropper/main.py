"""
0. install needed packages
    `py -m pip install PyPDF2` on Windows
    
1. fetch codes from the remote repository

2. arrange files as below
    pdf_cropper
    |-main.py
    |-dir01
    | |-file01.pdf
    | L-file02.pdf
    |-dir02
    :

3. run the following command
    `python3 main.py`

4. get an output folder as below
    pdf_cropper
    |-main.py
    :
    :
    L-pdf
     |-file01.pdf
     L-file02.pdf
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import os


DIR_NAME = 'dir01'
# by mm
UPPER_MARGIN = 30

dist = os.path.join(os.path.dirname(__file__), 'dist')


def crop_pdf(file: str):
    input_pdf = PdfFileReader(file)
    out_pdf = PdfFileWriter()

    # 1inch = 25.4mm = 72pt
    pt_per_mm = 72 / 25.4

    for i in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(i)
        # by pt
        right, upper = page.mediaBox.getUpperRight()
        page.cropBox.upperRight = (
            float(right), float(upper)-UPPER_MARGIN*pt_per_mm)

        out_pdf.addPage(page)

    out = os.path.join(dist, os.path.basename(file))

    with open(out, "wb") as fp:
        out_pdf.write(fp)


if __name__ == "__main__":
    os.makedirs(dist, exist_ok=True)

    files = glob.glob(
        os.path.join(os.path.dirname(__file__), DIR_NAME, "*.pdf")
    )
    for file in files:
        print("%s is being processed now." % os.path.basename(file))
        crop_pdf(file)
