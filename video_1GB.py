import cv2
import os
import math

def split_video(video_path, size_limit):
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    chunk_frame_count = math.ceil(size_limit / (video.get(cv2.CAP_PROP_FRAME_COUNT) / (width * height * 3)))

    os.makedirs("output", exist_ok=True)
    writer = None
    chunk_index = 0
    for i in range(frame_count):
        ret, frame = video.read()
        if not ret:
            break

        if i % chunk_frame_count == 0:
            if writer is not None:
                writer.release()
            chunk_index += 1
            filename = f"C:/Users/dbtmd/Videos/미래문화포럼-1GB/쪼갠파일/chunk{chunk_index}.avi"    # Output files will be in AVI format
            writer = cv2.VideoWriter(filename, fourcc, fps, (width, height))

        writer.write(frame)

    if writer is not None:
        writer.release()
    video.release()

video_path = "C:/Users/dbtmd/Videos/미래문화포럼-1GB/미래기술문화포럼.mp4"
size_limit = 1 * 1024 * 1024 * 1024  # 1 GB

split_video(video_path, size_limit)
