from ultralytics import YOLO

WEIGHTS = r"D:\vehicle\runs\train\licenseplate-yolov8s\weights\best.pt"
VIDEO   = r"D:\vehicle\vc1.MOV"   # ganti ke video kamu

model = YOLO(WEIGHTS)

model.predict(
    source=VIDEO,
    conf=0.25,
    imgsz=640,
    show=True,   # tampilkan hasil
    save=True    # simpan hasil ke runs/predict-...
)

print("Selesai. Cek folder runs/predict-... untuk video hasilnya.")
