from ultralytics import YOLO
import csv

# 載入模型
model = YOLO("yolov8n.pt")

# 影片追蹤
results = model.track(
    source=r"C:\Users\70808\Desktop\MOT17-08\input_video.mp4",
    tracker="bytetrack.yaml",
    classes=[0],      # person
    conf=0.3,
    show=True,
    stream=True
)

# 輸出 CSV
with open("crowd_density_area.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["frame", "num_people", "area_density"])

    for frame_idx, r in enumerate(results):
        num_people = len(r.boxes)

        # 影像面積
        h, w = r.orig_shape
        frame_area = h * w

        # 計算所有行人 bounding box 面積
        total_person_area = 0
        for box in r.boxes.xyxy:
            x1, y1, x2, y2 = box
            total_person_area += (x2 - x1) * (y2 - y1)

        # 人口密度（面積比例）
        area_density = total_person_area / frame_area

        writer.writerow([frame_idx, num_people, area_density])

        print(
            f"Frame {frame_idx}: "
            f"人數={num_people}, "
            f"面積密度={area_density:.6f}"
        )
