from pytube import YouTube
import uuid

class DownloadVideo:

    def __init__(self, ytLink):
        self.ytLink = ytLink

    def downloadVideo(self):
        yt = YouTube(self.ytLink)
        #TO DO Hardcoding video specs for now
        video = yt.get('mp4', '720p')
        uid = uuid.uuid1().urn
        yt.set_filename(yt.filename + '-' + uid[9:])
        print('Downloading video now, hold up....\n')
        video.download('YTDownloads/')
        print('Done downloading... ' + yt.filename + '\n')





    
