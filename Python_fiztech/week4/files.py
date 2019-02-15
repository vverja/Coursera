from os import path
import tempfile


class File():
    def __init__(self, file):
        self.file = open(file, 'r+')

    def write(self, text):
        self.file.seek(0, 2)
        self.file.write(text)
        self.file.seek(0, 0)

    def read(self):
        self.file.seek(0, 0)
        text = self.file.read()
        self.file.seek(0, 0)
        return text

    def __str__(self):
        return self.file.name

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line.rstrip()

    def __add__(self, second_file):
        newfile = File(path.join(tempfile.gettempdir(), "newfile"))
        text_of_first = self.read()
        if isinstance(second_file, File):
            text_of_second = second_file.read()
        else:
            text_of_second = str(second_file) + "\n"
        newfile.write(text_of_first + text_of_second)
        return newfile

    def __del__(self):
        self.file.close()
