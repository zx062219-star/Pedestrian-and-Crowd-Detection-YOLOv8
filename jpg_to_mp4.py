import cv2
import os

img_dir = r"C:\Users\70808\Desktop\MOT17-08\img1"
output = r"C:\Users\70808\Desktop\MOT17-08\input_video.mp4"

images = sorted(os.listdir(img_dir))
first = cv2.imread(os.path.join(img_dir, images[0]))
h, w, _ = first.shape

out = cv2.VideoWriter(
    output,
    cv2.VideoWriter_fourcc(*"mp4v"),
    30,  # FPS
    (w, h)
)

for img_name in images:
    frame = cv2.imread(os.path.join(img_dir, img_name))
    out.write(frame)

out.release()
print("影片產生完成:", output)
