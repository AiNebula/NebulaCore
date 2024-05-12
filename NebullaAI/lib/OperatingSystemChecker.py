import os
import platform

class OperatingSystemChecker:
    def __init__(self) -> None:
        self.operating_systems = {
            0   : "windows",
            1   : "linux",
            2   : "android",
            3   : "darwin"
        }

    def get_operating_system(self) -> int:
        if self.__is_android():
            return 2
        elif self.__is_windows():
            return 0
        elif self.__is_macos():
            return 3
        elif self.__is_linux():
            return 1
        
        raise Exception("Operating System in undefined")
    
    def get_operating_system_name(self) -> str:
        return self.operating_systems[self.get_operating_system()]

    def __is_windows(self) -> bool:
        """Checks if the operating system is Windows."""
        return os.path.exists('C:\\Windows\\System32')

    def __is_macos(self) -> bool:
        """Checks if the operating system is macOS."""
        return os.path.exists('/System/Library/CoreServices')
    
    def __is_linux(self) -> bool:
        """Checks for presence of common Linux directories."""
        return os.path.exists("/etc/os-release")
    
    def __is_android(self) -> bool:
        # Check for 'ANDROID_SDK_ROOT' for Android (common indicator)
        if 'ANDROID_SDK_ROOT' in os.environ:
            return True

        # Check for specific OS indicators in environment variables
        if 'PROCESSOR_ARCHITECTURE' in os.environ:
            arch = os.environ['PROCESSOR_ARCHITECTURE']
            if 'ARM' in arch.lower():  # Check for ARM architecture (common for Android/mobile)
                return True
        
        if 'android' in platform.uname().release.lower() or 'android' in platform.uname().version.lower():
            return True
        
        return False