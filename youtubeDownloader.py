from pytube import YouTube
import os
url = input("YouTube video link: ")
yt = YouTube(url)
print("Downloading", yt.title)
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
res = yt.streams.get_highest_resolution()
res.download(downloads_folder)
print("Download complete")
