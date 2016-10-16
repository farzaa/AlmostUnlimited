from imgurpython import ImgurClient
import urllib

class Imgur_Uploader(object):
    def __init__(self):
        client_id = 'b0bf6da0d2a7e8b'
        client_secret = '9a5fd6c74839a7a863e52868729b7ae4d8eb5223'

        self.client = ImgurClient(client_id, client_secret)
        
    def upload_image(self, filepath):
        return self.client.upload_from_path(filepath)

    def download_image(self, image_id, name):
        image = self.client.get_image(image_id)
        image_link = image.link
        urllib.urlretrieve(image_link, "IMGURDownloads/" + name)