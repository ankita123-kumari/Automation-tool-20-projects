from pytube import YouTube

def download_video(video_url, save_path="."):
    """Download a YouTube video in the highest resolution."""
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download(output_path=save_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage
video_link = input("Enter YouTube video URL: ")
download_video(video_link)