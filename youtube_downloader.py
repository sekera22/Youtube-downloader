from pytube import YouTube
def download_video(url, path):
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occured:", str(e))
url = input("Enter the Youtube video url: ")
path = input("Enter the output path to save the video: ")
download_video(url, path)