import datetime


class Logger:
    def __init__(self):
        self.file_name = str(datetime.datetime.now())+".txt"
        with open(self.file_name, "w"):
            pass

    def log(self, data):
        with open(self.file_name, "a") as f:
            f.write(f'{datetime.datetime.now()}: {data}\n')