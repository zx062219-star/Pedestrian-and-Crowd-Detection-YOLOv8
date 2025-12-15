# Crowd Density Estimation using YOLOv8 and ByteTrack

## Overview
This project detects and tracks pedestrians in surveillance video and estimates crowd density using an area-based metric.

## Objectives
- Detect pedestrians using YOLOv8
- Track multiple objects using ByteTrack
- Estimate crowd density based on pedestrian bounding box area

## Framework & Techniques
- **Framework:** PyTorch, Ultralytics YOLOv8
- **Techniques:** Bounding box regression, Non-Max Suppression (NMS), Area-based crowd density
- **Dataset:** MOT17 (video surveillance)

## Dataset
- **MOT17**: Multiple Object Tracking benchmark dataset  
- Source: [https://motchallenge.net/data/MOT17/](https://motchallenge.net/data/MOT17/)  
- Due to size and licensing restrictions, the dataset is **not included**.  
- To run this project, download the MOT17 dataset and place the frames in the folder referenced in `main.py` (e.g., `data/img1/`).

## Method
Pedestrians are detected using YOLOv8 and tracked across frames with ByteTrack.  
Crowd density is calculated as:


This metric reflects the proportion of the frame occupied by pedestrians.

## Project Structure
Pedestrian and Crowd Detection/
├─ main.py # Pedestrian detection, tracking, and crowd density calculation
├─ images_to_video.py # Convert PNG frames to video
├─ requirements.txt # Dependencies
├─ README.md # Project overview
├─ .gitignore # Files/folders to ignore


## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt

python jpg_to_mp4.py

python main.py


##Output

crowd_density_area.csv → per-frame pedestrian count and area-based density

output.mp4 → video with bounding boxes and tracking IDs