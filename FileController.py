class FileController:
    def __init__(self, filename):
        self.filename = filename
    
    def write_link(self, name, link):
        """
        Writes a video filename and link to the file associated
        with this object

        Args:
            name: A string representing the file name
            link: A string representing the youtube link
        """
        with open(self.filename, 'a') as file:
            file.write(name + '-' + link)
        
    