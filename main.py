import sys

from PySide import QtGui, QtCore
from PySide.QtGui import QFileDialog, QWidget, QMessageBox

from user_input import requestUserData
from FileController import FileController
from YouTubeUploader import upload
from download_video import DownloadVideo
from unlimitedui import Ui_Unlimited

class UnlimitedUi(QWidget, Ui_Unlimited):
    def __init__(self):
        """
        Initialize the GUI and connect buttons to functions
        """
        super(UnlimitedUi, self).__init__()
        self.setupUi(self)
        
        self.browse_button.clicked.connect(self.browse_file)
        self.upload_button.clicked.connect(self.upload_file)
        self.show()

    def upload_file(self):
        """
        Takes data from the text boxes. If there is enough info, the video
        is uploaded. A dialog opens when complete
        """
        fileName = self.filename_text.text()
        description = self.description_text.text()
        title = self.title_text.text()

        if not (fileName and description and title):
            return

        category = '22'
        keywords = 'empty'
        privacyStatus = 'unlisted'

        args = {'fileName': fileName, 'title': title, 'description': description, 'category:': category,
            'keywords': keywords, 'privacyStatus': privacyStatus}
        
        upload(args)
        msgBox = QMessageBox()
        msgBox.setText("File uploaded.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        ret = msgBox.exec_()

    def browse_file(self):
        """
        Opens file browser to select video file
        """
        print 'pressed'
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '~/', 'Video Files (*.mp4)')
        self.filename_text.insert(fname)
        

def main():
    print 'Hello, world!'

def outputMenu():
    print("Welcome to the AlmostUnlimitedStorage Cloud\n")
    print("Type UP to upload a new video\n")
    print("Type DOWN to download a video that has already been uploaded to our cloud\n")
    print("Type QUIT to quit\n")
    print 'Type CLEAR to clear saved videos\n'

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    unlimited_ui = UnlimitedUi()
    sys.exit(app.exec_())

    # File Controller with Dict from JSON file
    file_controller = FileController()
    file_controller.process_json()