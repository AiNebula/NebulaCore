from NebullaAI.lib.OperatingSystemChecker import OperatingSystemChecker
from NebullaAI.lib.BathBuilder import BathBuilder
import os
import shutil

class FolderController:
    def __init__(self) -> None:
        # getting operating system name
        self.operatin_system = OperatingSystemChecker().get_operating_system_name()
    
    # consider refactoring the android code
    def __android_command(self, foldername:str, location:str) -> bool:
        return False
    
    def create_folder(self, foldername:str, location:str) -> bool:
        if type(foldername) != str or type(location) != str: raise ValueError("foldername, and location must be of type String")
        if self.operatin_system == 'android':
            if getattr(self, f"_FolderController__{self.operatin_system}_command")(foldername, location): return True
        # build path
        path = BathBuilder().build(location)
        try:
            # write create folder logic
            os.mkdir(f"{path}\\{foldername}")
            return True
        except FileExistsError as e:
            raise FileExistsError(f"{foldername} is already exists in {path}")
        except OSError as e:
            raise Exception(f"{self} can't create folder {foldername} in {location}.")
    
    def delete_folder(self, foldername:str, location:str) -> bool:
        # check strings
        if type(foldername) != str or type(location) != str: raise ValueError("foldername, and location must be of type String")
        # check android
        if self.operatin_system == 'android':
            if getattr(self, f"_FolderController__{self.operatin_system}_command")(foldername, location): return True
        # build path
        path = BathBuilder().build(location)
        # check directory
        if not os.path.isdir(path) : raise Exception(f"{path} is not a Directory.")
        # check folder existnace
        if not os.path.exists(os.path.join(path, foldername)): raise FileExistsError(f"{foldername} isn't exist in {location}.")
        # delete file if exist
        try:
            os.removedirs(os.path.join(path, foldername))
            return True
        except PermissionError as e:
            raise PermissionError(f"it is not permitted to delete {path}")
        except WindowsError as e:
            # checking if it is not empty
            if e.winerror == 145:
                ask = input(f"{os.path.join(path, foldername)} in not empty, it contains {os.listdir(os.path.join(path, foldername))}, do you want to remove it ?. press Y to Confirm, or Press any key to cancell.")
                # create a dynamic helper system as an enhancment for handeling conversation
                if ask.lower() == 'y':
                    shutil.rmtree(os.path.join(path, foldername), True, None)
                    return True
                return False
            raise Exception(f"Can't remove {foldername} folder.")
    
    def move_folder(self, foldername:str, source:str, destination:str) -> bool:
        # check the strings
        if type(foldername) != str or type(source) != str or type(destination) != str: raise ValueError("foldername, and location must be of type String")
        # check android
        if self.operatin_system == 'android':
            # refactor android code
            if getattr(self, f"_FolderController__{self.operatin_system}_command")(foldername, source, destination): return True
        # build path
        bb = BathBuilder()
        source_path = bb.build(source)
        destination_path = bb.build(destination)
        # check directory
        if not os.path.isdir(source_path) : raise Exception(f"{source} is not a Directory.")
        if not os.path.isdir(destination_path) : raise Exception(f"{destination} is not a Directory.")
        # handeling nested folder destintaion path
        if not os.path.exists(os.path.join(source_path, foldername)): raise FileExistsError(f"{foldername} isn't exist in {source_path}")
        if not os.path.exists(destination_path): raise FileNotFoundError(f"{destination_path} isn't exist.")
        # move file if exists
        try:
            shutil.move(os.path.join(source_path, foldername), os.path.join(destination_path, foldername))
            return True
        except PermissionError as e:
            raise PermissionError(f"moving '{foldername}' from '{source_path}' to '{destination_path}' isn't premitied.")

    