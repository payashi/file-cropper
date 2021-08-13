# File Cropper

## PDF Cropper

1. install needed packages

```bash
   py -m pip install PyPDF2
```
   
2. fetch codes from [here](https://github.com/payashi/file-cropper/blob/main/pdf_cropper/main.py)

3. arrange files as below

```bash
    pdf_cropper
    ├── dir01
    │   └── file01.pdf
    └── main.py
```

4. set `DIR_NAME` and `UPPER_MARGIN`

5. run `python3 main.py`

6. get an output folder as below

```bash
    pdf_cropper
    ├── dir01
    │   └── file01.pdf
    ├── dist
    │   └── file01.pdf
    └── main.py
```

## DICOM Cropper

1. install needed packages
```bash
   py -m pip install pydicom matplotlib numpy pylibjpeg pylibjpeg-libjpeg
```

2. fetch codes from [here](https://github.com/payashi/file-cropper/blob/main/dcm_cropper/main.py)

3. arrange files as below

```bash
    dcm_cropper
    ├── dir01
    │   └── file01.dcm
    └── main.py
```

4. set `UPPER`, `LOWER`, `LEFT`, `RIGHT` and `DIR_NAME`

5. run `python3 main.py`

6. get output folders as below

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
