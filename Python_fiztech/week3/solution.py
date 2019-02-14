
class FileReader(object):
    """This class is for reading files"""
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            f = open(self.filename)
            return(f.read())
        except IOError:
            return ""
