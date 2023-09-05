import pytube
from pytube.cli import on_progress
import shutil

link = ''                # input link of the video you want to download

videoDownload = pytube.YouTube(link, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)

title = videoDownload.title

print(title)
print(f"Video length in minutes: {videoDownload.length/60}")
print(f"Video length in seconds: {videoDownload.length}")
print(f"Number of views: {videoDownload.views}")

mega_byte = videoDownload.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().filesize

print(f"Video download size: {round(mega_byte/1048576)}MB")
print(f"{videoDownload.title} by {videoDownload.author} downloading...")
print(f"{title} download complete!")




# the downloaded video is stored in this direcrtory. if you want to move the video to another location, uncomment the below code

# source = f'{title}.mp4'
# destination = f''      # absolute path of the directory you want the video to be saved to

# download = videoDownload.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# shutil.move(download, destination)

# print('File moved successfully!')
