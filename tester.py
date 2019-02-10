import os
import serverCommunication
import smtp

class test_main():
    def __init__(self):
        self.total_used_size = 0
        self.total_rem_size = 0
        self.total_size = 5    # Total size provided is 10 bytes. OG is 10 Gb

    def calculate_size_of_folder(self, start_path):
        os.chdir(start_path)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                self.total_used_size += os.path.getsize(os.path.join(root, name))

    def get_size_in_kb(self, start_path):
        self.calculate_size_of_folder(start_path)
        return self.total_used_size

    def get_rem_size_in_kb(self, start_path):
        self.calculate_size_of_folder(start_path)
        self.total_rem_size = self.total_size - self.total_used_size
        return self.total_size - self.total_used_size

    def get_rem_percentage(self, start_path):
        self.get_rem_size_in_kb(start_path)
        return round(((self.total_rem_size / self.total_size) * 100), 2)

    def test_full_storage(self):
        rem_storage_percent = 12
        if rem_storage_percent < 15:
            smtp.send("VBAC NAS Storage Message", "Your VBAC NAS unit currently has %s percent of remaining storage."
                      % rem_storage_percent)
        return
