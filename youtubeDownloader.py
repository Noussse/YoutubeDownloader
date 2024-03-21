from pytube import YouTube
url = input("YouTube video link: ")
yt = YouTube(url)
print("Downloading", yt.title)
res = yt.streams.get_highest_resolution()
res.download(r'C:\Users\nouss\Downloads')
print("download comlete")