from .OperatingSystemChecker import OperatingSystemChecker
import os
import re

class BathBuilder:
    """
    Building path based on the running system, and handelling
    if the path is a nested path
    """
    
    def __init__(self, system:object=None) -> None:
        self.operating_systems = {
            0   : "windows",
            1   : "linux",
            2   : "android",
            3   : "darwin"
        }
        self.path = ""
        self.__seperators = ['/', '\\']
        # self.system_source = system.source_system
        self.operating_system = OperatingSystemChecker().get_operating_system()
        self.common_locations = ["desktop", "documents", "downloads", "pictures", "videos", "music"]
    
    # building the full path
    def build(self, directory:str) -> str:

        # check if it is nested path
        if self.__check_seperators(directory): return self.__build_path(directory)

        # check if it is in the common locations
        if directory.lower() in self.common_locations:
            return f"{self.get_base_path()}\\{directory}"
        else:
            # if it is not in the common location, build a new path
            if self.path != "":
                return f"{self.path}\\{directory}"
            return f"{self.path}{directory}"
        
        # that is working and raising doesn't have any effect if the code
        # raise Exception(f"Can't build path for {directory}")
        
    # Building a new path if the path isn't in the common paths
    def __build_path(self, path:str):

        dirs = path.split(self.sep)
        for _dir in dirs:
            self.path = self.build(_dir)
        return self.path

    # make ia a file extention
    def filename_extention(self, filename:str, extention:str) -> str:

        common_extentions = [".png", ".jpg", ".jpeg", ".txt", ".docx"]
        if filename.endswith(tuple(common_extentions)):
            return re.sub(r"[:.-]", "", filename) + extention
        return re.sub(r"[:.-]", "",filename) + extention

    # getting the base path if it is in the common paths
    def get_base_path(self):

        if self.operating_systems[self.operating_system] == "windows":
            try:
                path = os.environ['USERPROFILE']
                return path
            except KeyError:
                return "C:\\Users\\" + os.environ['USERNAME']
        elif self.operating_systems[self.operating_system] == "linux":
            return "/Users/" + os.environ['SHORTNAME']
        elif self.operating_systems[self.operating_system] == "darwin":
            return "/Users/" + os.environ['SHORTNAME']
        elif self.operating_systems[self.operating_system] == "android":
            # getting paths in mobile
            pass

        return None
    
    # check if the path in nested
    def __check_seperators(self, path:str) -> bool:

        for sep in self.__seperators:
            if sep in path:
                self.sep = sep
                return True
        return False