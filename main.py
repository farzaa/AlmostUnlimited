import sys
import qdarkstyle

from PySide import QtGui, QtCore
from PySide.QtGui import QFileDialog, QWidget, QMessageBox

from user_input import requestUserData
from FileController import FileController
from YouTubeUploader import upload
from download_video import DownloadVideo
from unlimitedui import Ui_Unlimited
from Imgur_Uploader import Imgur_Uploader

class UnlimitedUi(QWidget, Ui_Unlimited):
    def __init__(self):
        """
        Initialize the GUI and connect buttons to functions
        """
        super(UnlimitedUi, self).__init__()
        self.setupUi(self)
        
        self.browse_button.clicked.connect(self.browse_file)
        self.upload_button.clicked.connect(self.upload_file)
        self.download_button.clicked.connect(self.download_file)
        self.show()

        self.filenameToLink = dict()
        self.imgur_uploader = Imgur_Uploader()    

    def get_uploads(self):
        """
        Takes all of the data from the google docs sheet to populate
        the combo box
        """
        # Replace this line with an actual function call when it is implemented
        self.filenameToLink = SomeFunctionThatReturnsDictOfFilesAndLinks()
        # Add the filenames to the combobox
        self.uploaded_combo.addItems(self.filenameToLink.keys())

    def download_file(self):
        """
        Takes whatever text the combobox is showing. Either uses the imgur or youtube
        download methods depending on the file extension
        """
        filename = self.uploaded_combo.currentText()
        if filename in self.filenameToLink:
            if filename[-3:] == 'mp4':
                dv = DownloadVideo(self.filenameToLink[filename])
                dv.downloadVideo()
            else:
                self.imgur_uploader.download_image(self.filenameToLink[filename], filename)

            msgBox = QMessageBox()
            msgBox.setText("File downloaded.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            ret = msgBox.exec_()
        

    def upload_file(self):
        """
        Takes data from the text boxes. If there is enough info, the video
        is uploaded. A dialog opens when complete
        """
        fileName = self.filename_text.text()
        description = self.description_text.text()
        title = self.title_text.text()

        if fileName[-3:] == 'png' or fileName[-3:] == 'jpg':
            smallName = fileName.split('/')[-1]
            self.uploaded_combo.addItem(smallName)

            result = self.imgur_uploader.upload_image(fileName)
            self.filenameToLink[smallName] = result['id']
            print 'Image upload: ', result
            return

        if not (fileName and description and title):
            return
        
        category = '22'
        keywords = 'empty'
        privacyStatus = 'unlisted'

        args = {'fileName': fileName, 'title': title, 'description': description, 'category:': category,
            'keywords': keywords, 'privacyStatus': privacyStatus}
        
        videoUrl = upload(args)

        msgBox = QMessageBox()
        msgBox.setText("File uploaded.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        ret = msgBox.exec_()

        smallName = fileName.split('/')[-1]
        self.uploaded_combo.addItem(smallName)
        self.filenameToLink[smallName] =  r'https://www.youtube.com/watch?v=' + videoUrl

        # Upload link and filename to the google doc

    def browse_file(self):
        """
        Opens file browser to select video file
        """
        
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '~/', 'Media Files (*.mp4 *.png *.jpg)')
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
    #db = Backend()
    #db.init

    #sys.exit(app.exec_())

    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    unlimited_ui = UnlimitedUi()
    sys.exit(app.exec_())

    # File Controller with Dict from JSON file
    file_controller = FileController()
    file_controller.process_json()