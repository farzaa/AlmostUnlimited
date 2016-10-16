from user_input import requestUserData
from FileController import FileController
from YouTubeUploader import upload

def main():
    print 'Hello, world!'

def outputMenu():
    print("Welcome to the AlmostUnlimitedStorage Cloud\n")
    print("Type UP to upload a new video\n")
    print("Type DOWN to download a video that has already been uploaded to our cloud\n")
    print("Type QUIT to quit\n")

 
if __name__ == '__main__':
    quitMenu = False
    outputMenu()
    input = raw_input('INPUT HERE:\n')
    print(input)
    while(not quitMenu):
        input = raw_input('INPUT HERE:\n')

        if input in 'UP':
            #Run API upload methods 
            print('Upload Tool...\n')	
            upload(requestUserData())
        if input in 'DOWN':
            #Run download 
            print('Download Tool...\n')

        if input in 'QUIT': 
        	quitMenu = True;
        	
    outputMenu()




