from moviepy.editor import VideoFileClip

def convert_video_to_gif(video_path, output_gif):
    """Convert a video file to GIF format."""
    clip = VideoFileClip(video_path)
    clip.write_gif(output_gif, fps=10)  # Adjust FPS for smoother GIF

# Example Usage
video_file = "example.mp4"  # Replace with your video file
gif_file = "output.gif"
convert_video_to_gif(video_file, gif_file)

print("GIF conversion completed successfully!")