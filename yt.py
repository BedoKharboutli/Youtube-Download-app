from pytube import YouTube
from sys import argv

link = argv[1]

# here we check on video's title and views
try:
    youtube = YouTube(link)
    print("TITLE:", youtube.title)
    print("VIEWS :", youtube.views)
    # get the highest video quality as possible
    youtube_download = youtube.streams.get_highest_resolution()
    # the path or file where the video will be downloaded at
    youtube_download.download("/Users/bedokharboutli/Desktop/Projects/youtube-download")
except Exception as e:
    print("An error occurred:", e)
