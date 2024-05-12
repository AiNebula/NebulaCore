from NebullaAI.lib.OperatingSystemChecker import OperatingSystemChecker
from NebullaAI.lib.BathBuilder import BathBuilder
import os
import shutil

class FileController:
    def __init__(self) -> None:
        # getting operating system name
        self.operatin_system = OperatingSystemChecker().get_operating_system_name()
    
    # consider refactoring the android code
    def __android_command(self, filename:str, location:str) -> bool:
        return False
    
    def create_file(self, filename:str, location:str, content="") -> bool:
        if type(filename) != str or type(location) != str: raise ValueError("filename, and location must be of type String")
        if self.operatin_system == 'android':
            if getattr(self, f"_FileController__{self.operatin_system}_command")(filename, location): return True
        
        path = BathBuilder().build(location)
        if '.' not in filename: filename = f"{filename}.txt"
        try:
            with open(os.path.join(path, filename), 'w') as file:
                print(f"createing {filename} file in {path}")
                file.write(content)
            return True
        except OSError as e:
            raise Exception(f"{self} can't create file {filename} in {location}.")
    
    def delete_file(self, filename:str, location:str, content="") -> bool:
        # check strings
        if type(filename) != str or type(location) != str: raise ValueError("filename, and location must be of type String")
        # check android
        if self.operatin_system == 'android':
            if getattr(self, f"_FileController__{self.operatin_system}_command")(filename, location): return True
        # build path
        path = BathBuilder().build(location)
        # check extention
        if '.' not in filename: raise Exception("Extention of the file is not Provided.")
        # check file existnace
        if not os.path.exists(os.path.join(path, filename)): raise FileExistsError(f"{filename} isn't exist in {location}.")
        # delete file if exist
        try:
            os.remove(os.path.join(path, filename))
            return True
        except PermissionError as e:
            raise PermissionError(f"it is not permitted to delete {path}")
    
    def move_file(self, filename:str, source:str, destination:str) -> bool:
        # check the strings
        if type(filename) != str or type(source) != str or type(destination) != str: raise ValueError("filename, and location must be of type String")
        # check android
        if self.operatin_system == 'android':
            # refactor android code
            if getattr(self, f"_FileController__{self.operatin_system}_command")(filename, source, destination): return True
        # build path
        bb = BathBuilder()
        source_path = bb.build(source)
        destination_path = bb.build(destination)
        # check extentions
        if '.' not in filename: raise Exception("Extention isn't provided in the filename.")
        # handeling nested folder destintaion path
        if not os.path.exists(os.path.join(source_path, filename)): raise FileExistsError(f"{filename} isn't exist in {source_path}")
        if not os.path.exists(destination_path): raise FileNotFoundError(f"{destination_path} isn't exist.")
        # move file if exists
        try:
            shutil.move(os.path.join(source_path, filename), os.path.join(destination_path, filename))
            return True
        except PermissionError as e:
            raise PermissionError(f"moving '{filename}' from '{source_path}' to '{destination_path}' isn't premitied.")
    