import os

class Singleton():
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
    return cls.instance
   

class FileManager(Singleton):
    def __init__(self):
        self.root_directory = os.getcwd()

    def change_directory(self, new_directory):
        """Change the current root directory."""
        if os.path.isdir(new_directory):
            self.root_directory = new_directory
        else:
            print(f"The directory {new_directory} doesn't exist!")

    def list_directories(self):
        """List sub-directories in the current root directory."""
        with os.scandir(self.root_directory) as it:
            return [entry.name for entry in it if entry.is_dir()]

    def list_files(self):
        pass

    def create_file(self, file_name, content=""):
        pass

    def read_file(self, file_name):
        pass




file_manager1 = FileManager()
file_manager2 = FileManager()

print(file_manager1 is file_manager2)

print(file_manager1.list_directories(), " - First manager")
print(file_manager2.list_directories(), " - Second manager")

file_manager1.change_directory("./Code")

print(file_manager1.list_directories(), " - First manager")
print(file_manager2.list_directories(), " - Second manager")
