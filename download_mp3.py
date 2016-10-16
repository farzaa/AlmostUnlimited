from __future__ import unicode_literals
import youtube_dl


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def downloadMP3(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            #We can look into higher audio qualities another time. Not sure how this affects youtube_dl
            'preferredquality': '192',
        }],
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


