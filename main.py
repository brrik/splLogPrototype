### this program needs OpenCV and numpy
### also, os systems are required
import cv2
import os

def save_frame(video_path, result_path):
    cap = cv2.VideoCapture(video_path)

    flameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(flameCount)

    for i in range(flameCount):
        if i%6 == 0:
            if not cap.isOpened():
                return

            flames = i
            os.makedirs(os.path.dirname(result_path), exist_ok=True)

            cap.set(cv2.CAP_PROP_POS_FRAMES, flames)

            ret, frame = cap.read()
            result_name = "img_"+str(i)+".jpg"
            result_fullpath = result_path + result_name

            if ret:
                cv2.imwrite(result_fullpath, frame)

save_frame('origin/1080p.mp4', 'jpg/')