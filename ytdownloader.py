import os.path
from pytube import YouTube
from sys import argv
from pytube.cli import on_progress

link = argv[1]  # index 0 - script name // index 1 - link to video to download
yt = YouTube(link, on_progress_callback=on_progress)  # YouTube object with progress bar
yt.check_availability()  # check availability

try:  # exception handling in case second parameter is not provided
    is_video = argv[2]
    if is_video == "V":  # get highest quality for that video
        yd = yt.streams.get_highest_resolution()
    elif is_video == "M":  # get audio only for link provided
        yd = yt.streams.get_audio_only()
except IndexError:  # print usage
    print("Missing 2nd argument!!\nV - video (high quality)\nM - music (audio only)")
    exit(0)

print(f"Title: {yt.title}\nViews: {yt.views}\nLength: {yt.length / 60:.2f} min")  # basic informations about file
print(f"Filesize: {yd.filesize / 1048576:.2f} MB")

# if file already exists ask user if sure to download same file once again
if os.path.exists(f'/mnt/c/Users/sebas/OneDrive/Desktop/YT_Downloads/{yt.title}.mp4'.strip(" \n")):
    choice = input("File about to be downloaded arleady exists. Want to download anyway?\ny/n ")
    if choice != "y":
        exit(0)

yd.download("/mnt/c/Users/sebas/OneDrive/Desktop/YT_Downloads")  # download to given folder
print("\nDownload completed!")

