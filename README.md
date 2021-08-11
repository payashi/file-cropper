# File Cropper

## PDF Cropper

0. install needed packages
   `py -m pip install PyPDF2` on Windows
1. fetch codes from the remote repository

2. arrange files as below

```bash
    pdf_cropper
    ├── dir01
    │   └── file01.pdf
    └── main.py
```

3. set `DIR_NAME` and `UPPER_MARGIN`

4. run `python3 main.py`

5. get an output folder as below

```bash
    pdf_cropper
    ├── dir01
    │   └── file01.pdf
    ├── dist
    │   └── file01.pdf
    └── main.py
```

## DICOM Cropper

0. install needed packages
   `py -m pip install pydicom matplotlib numpy pylibjpeg` on Windows

1. fetch codes from the remote repository

2. arrange files as below

```bash
    dcm_cropper
    ├── dir01
    │   └── file01.dcm
    └── main.py
```

3. set `UPPER`, `LOWER`, `LEFT`, `RIGHT` and `DIR_NAME`

4. run the following command
   `python3 main.py`

5. get output folders as below

```bash
    dcm_cropper
    ├── dir01
    │   └── file01.dcm
    ├── dcm
    │   └── file01.dcm
    ├── png
    │   └── file01.png
    ├── npy
    │   └── file01.npy
    └── main.py
```
