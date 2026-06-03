from moviepy.editor import VideoFileClip
import os

input_path = "6月2日社团活动宣传.mp4"
output_path = "video_compressed.mp4"

print("正在加载视频...")
clip = VideoFileClip(input_path)

# 目标：压缩到25MB以内
# 计算目标码率 (bits per second)
target_size_mb = 24  # 留一点余量
target_size_bits = target_size_mb * 8 * 1024 * 1024
duration = clip.duration
target_bitrate = int(target_size_bits / duration)

print(f"视频时长: {duration:.1f}秒")
print(f"目标码率: {target_bitrate // 1000} kbps")
print("正在压缩...")

# 压缩：降低分辨率到720p，降低码率
w, h = clip.size
if h > 720:
    new_h = 720
    new_w = int(w * new_h / h)
    clip = clip.resize(newsize=(new_w, new_h))

clip.write_videofile(
    output_path,
    bitrate=f"{target_bitrate}",
    codec="libx264",
    audio_codec="aac",
    threads=4,
    preset="fast",
    ffmpeg_params=["-movflags", "+faststart"]
)

clip.close()

size_mb = os.path.getsize(output_path) / (1024 * 1024)
print(f"压缩完成！文件大小: {size_mb:.2f} MB")
