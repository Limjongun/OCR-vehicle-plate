from ultralytics import YOLO

WEIGHTS = r"D:\vehicle\runs\train\licenseplate-yolov8s\weights\best.pt"
FOLDER  = r"D:\vehicle\plattest"   # folder berisi jpg/png

model = YOLO(WEIGHTS)
model.predict(
    source=FOLDER,
    conf=0.25,
    imgsz=640,
    save=True,      
    show=False,
    save_crop=False # True kalau mau crop plat
)
print("Selesai. Cek folder runs/predict-... untuk hasilnya.")
