from imgurpython import ImgurClient
import urllib
import uuid

class Imgur_Uploader(object):
    def __init__(self):
        client_id = 'YOUR-CLIENT-ID'
        client_secret = 'YOUR-CLIENT-SECRET'

        self.client = ImgurClient(client_id, client_secret)
        
    def upload_image(self, filepath):
        return self.client.upload_from_path(filepath)

    def download_image(self, image_id, name):
        image = self.client.get_image(image_id)
        image_link = image.link
        uid = uuid.uuid1().urn
        urllib.urlretrieve(image_link, "IMGURDownloads/" + name[:-4] + uid[9:] + name[-4:])
        