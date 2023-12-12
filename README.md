# Parking Detection Hub
Parking detection with TinyML

This repository contains the code that runs on a "hub" device the automatic parking detection system. Right now, this repo houses an implementation of a keras-OCR-based plate recognition pipeline, as well as code to run the hub server to listen for plate images sent by parking detection "meter" devices.

## Instructions to Run

### 1. Clone source and enter into the directory.
```
git clone https://github.com/nlitz88/parkingdetection_hub.git
cd ./parkingdetection_hub
```

### 2. Create new Python virtual environment and activate it
```
python3 -m venv venv
source ./venv/bin/activate
```
### 3. Install dependencies
pip install -r requirements.txt

### 4. Run The Server
...
