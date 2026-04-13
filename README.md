# OCR VEHICLE PLATE DETECTION PROJECT

This project detects vehicle license plates using YOLO and reads the text using OCR.

---

1. REQUIREMENTS

---

Make sure you have Python 3.8+ installed.

Install required libraries:
pip install ultralytics
pip install opencv-python
pip install pytesseract
pip install numpy

(Optional for better OCR)
pip install easyocr

---

2. INSTALL YOLO (ULTRALYTICS)

---

You can use YOLOv8 from Ultralytics:

pip install ultralytics

Check installation:
python -c "from ultralytics import YOLO"

---

3. PROJECT STRUCTURE

---

ocr-vehicle-plate/
│
├── datasets/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│   └── data.yaml
│
├── runs/                (auto-generated, ignore)
├── detect.py            (YOLO detection script)
├── ocr.py               (OCR processing script)
├── train.py             (training script)
├── requirements.txt
└── README.txt

---

4. DATASET CONFIG (data.yaml)

---

Example data.yaml:

path: datasets
train: images/train
val: images/val

names:
0: plate

---

5. TRAIN MODEL

---

Run training using YOLO:

python train.py

Or directly with Ultralytics CLI:

yolo task=detect mode=train model=yolov8n.pt data=datasets/data.yaml epochs=50

---

6. RUN DETECTION

---

Run detection:

python detect.py

Or:

yolo task=detect mode=predict model=best.pt source=your_image.jpg

---

7. OCR PROCESS

---

After detecting the plate area:

* Crop the detected bounding box
* Send it to OCR (Tesseract / EasyOCR)

Example:
python ocr.py

---

8. NOTES

---

* Do NOT upload:

  * datasets/
  * runs/
  * *.pt (model files)
* Use external storage (Google Drive) for large files

---

9. FUTURE IMPROVEMENTS

---

* Improve OCR accuracy
* Add real-time camera detection
* Deploy to web/mobile app

---

This project is for learning and experimenting with AI-based license plate recognition.
