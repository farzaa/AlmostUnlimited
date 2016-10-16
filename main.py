from user_input import requestUserData
from FileController import FileController
from YouTubeUploader import upload
from download_video import DownloadVideo

def main():
    print 'Hello, world!'

def outputMenu():
    print("Welcome to the AlmostUnlimitedStorage Cloud\n")
    print("Type UP to upload a new video\n")
    print("Type DOWN to download a video that has already been uploaded to our cloud\n")
    print("Type QUIT to quit\n")
    print 'Type CLEAR to clear saved videos\n'

if __name__ == '__main__':
    dlvid = DownloadVideo('https://www.youtube.com/watch?v=fyBO3PTiZXc')
    dlvid.downloadVideo()
    quitMenu = False
    outputMenu()
    file_controller = FileController()
    file_controller.process_json()

    while(not quitMenu):
        input = raw_input('INPUT HERE:\n')

        if input in 'UP':
            #Run API upload methods 
            print('Upload Tool...\n')	
            upload(requestUserData())

        elif input in 'DOWN':
            #Run download 
            print('Download Tool...\n')
            file_controller.print_uploads()                    
            
            video_name = raw_input('Enter desired video:')
            link = file_controller.return_link(video_name)

            if link:
                # The link is valid
                # Call the download code
                pass
            else:
                print 'Invalid video, cannot download'

        elif input in 'QUIT': 
        	quitMenu = True
        	
        elif input in 'CLEAR':
            file_controller.clear_links()

    outputMenu()




