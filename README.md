# parkingdetection
Parking detection with TinyML

This repository currently houses an implementation of a keras-OCR-based plate
recognition pipeline, as well as code to run an flask server to make this
pipeline accessible via HTTP.

## Instructions to Run

### 1. Clone source and enter into the directory.
```
git clone https://github.com/nlitz88/parkingdetection.git
cd ./parkingdetection
```

### 2. Create new Python virtual environment and activate it
```
python3 -m venv venv
source ./venv/bin/activate
```

### 3. Update: Install PyTorch separately first.
https://pytorch.org/get-started/locally/

### 4. Install other dependencies
pip install -r requirements.txt

### 5. Run The Server
...