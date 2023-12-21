# Parking Detection Hub
Parking detection with TinyML

This repository contains the code that runs on a "hub" device the automatic
parking detection system. Right now, this repo contains the HTTP server code to
listen for plate images from "meter" devices and pass them through an EasyOCR
model for plate number recognition.

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

### 3. Install PyTorch separately before installing other requirements. 
Installing PyTorch can look a bit different depending on what kind of platform
you're working on, so it's best to consult their documentation and install
it separately, first.
https://pytorch.org/get-started/locally/

### 4. Install other dependencies
```
pip install -r requirements.txt
```
### 5. Run The Development Server
```
python demo_server.py
```