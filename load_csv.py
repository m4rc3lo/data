import unicodecsv

class Load_csv:

    def __init__(self, path, op):
        self.file_path = path
        self.operation = op

    def open(self):
        with open(self.file_path, self.operation) as f:
            reader = unicodecsv.DictReader(f)
            return list(reader)