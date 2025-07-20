from pytube import YouTube

link = YouTube("https://www.youtube.com/watch?v=0iAUbvsl6UQ")

video = link.streams.get_highest_resolution()

video.download()