import os


# All sizes are in bytes
class serverCommands():
    def __init__(self):
        self.total_used_size = 0
        self.total_rem_size = 0
        self.total_size = 1000000000    # Total size provided is 1 GB

    def calculate_size_of_folder(self, start_path):
        old_dir = os.getcwd()
        os.chdir(start_path)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                self.total_used_size += os.path.getsize(os.path.join(root, name))
        os.chdir(old_dir)
    # Used size methods
    def get_size_in_kb(self, start_path):
        self.calculate_size_of_folder(start_path)
        return self.total_used_size

    def get_size_in_mb(self, start_path):
        self.calculate_size_of_folder(start_path)
        return self.total_used_size / 1000000

    def get_size_in_gb(self, start_path):
        self.calculate_size_of_folder(start_path)
        return self.total_used_size / 1000000000

    # Remaining size methods
    def get_rem_size_in_kb(self, start_path):
        self.calculate_size_of_folder(start_path)
        self.total_rem_size = self.total_size - self.total_used_size
        return self.total_size - self.total_used_size

    def get_rem_size_in_mb(self, start_path):
        self.get_rem_size_in_kb(start_path)
        return self.total_rem_size / 1000000

    def get_rem_size_in_gb(self, start_path):
        self.get_rem_size_in_kb(start_path)
        return self.total_rem_size / 1000000000

    # Remaining percentage to two decimal places
    def get_rem_percentage(self, start_path):
        self.get_rem_size_in_kb(start_path)
        return round(((self.total_rem_size / self.total_size) * 100), 2)


if __name__ == '__main__':
    c = serverCommands()
    print(c.get_rem_percentage("/home/victor/Documents/IMAGES"))
