import tempfile

class Tmp_service:
    def __init__(self, file_data):
        self.file_data = file_data
        self.tmp_file = tempfile.NamedTemporaryFile(delete=False)
        self.tmp_name = ''


    def create_tmp_file(self):
        try:
            self.tmp_file.write(self.file_data)
            self.tmp_file.seek(0)
            self.tmp_name = self.tmp_file.name
        finally:
            self.tmp_file.close()
