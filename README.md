# youtube-downloader

main code 

import youtube_indir as downloader

link = input("Link")
v = downloader.Video(link) 
v.download()

v2 = downloader.Video("https://youtu.be/pJRzKOqxQJ0")
v2.description()
