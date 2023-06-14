from moviepy.editor import VideoFileClip
import os

def split_video_with_audio(video_path, size_limit):
    # Load video
    video = VideoFileClip(video_path)
    duration = video.duration
    fps = video.fps
    size_per_second = size_limit / duration

    # Create output directory
    os.makedirs("output", exist_ok=True)

    # Split video based on size limit
    start_time = 0
    chunk_index = 1
    while start_time < duration:
        # Calculate end time for current chunk
        end_time = start_time + size_per_second / fps

        # Ensure end time does not exceed video duration
        if end_time > duration:
            end_time = duration

        # Generate output file name
        output_file = f"output/chunk{chunk_index}.avi"

        # Cut video chunk and save
        video_chunk = video.subclip(start_time, end_time)
        video_chunk.write_videofile(output_file, codec='libx264')

        # Update start time and chunk index
        start_time = end_time
        chunk_index += 1

    print("영상을 성공적으로 분할했습니다. 확인해보세요.")

# Modify the values below to match your needs
video_path = "video.mp4"
size_limit = 1 * 1024 * 1024 * 1024   # 1 GB
split_video_with_audio(video_path, size_limit)

