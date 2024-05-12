import platform
import os
from NebullaAI.Services import SystemServices, FileServices

class SystemController:
    def __init__(self, orders:dict) -> None:
        self.system_info = platform.uname()
        self.system_level = self.__get_operating_system_level()
        self.orders = self.__check_orders(orders)
        self.__distribute()
    
    def __distribute(self):
        for lvl, item in self.orders.items():
            if lvl == "<lvl2>":
                # runs the lvl2 system for gemini
                pass
            elif lvl == self.__get_level():
                self.__sub_system()(lvl, item['tags'])
    
    def __sub_system(self):
        class SubSystemController:
            orders = self.orders
            system_info = self.system_info
            source_system = self.system_level

            def __init__(self, target_system:str, tags:list):
                self.target_system = target_system
                self.tags = tags
                self.__compile()
            
            def __compile(self):
                for service in self.tags:
                    print(f"source_system {self.source_system}, target_system : {self.target_system}")
                    self.__load_service(service=service[0], service_tags=service[1:])

            def __load_service(self, service:str, service_tags:list):
                print("Loading Servive : ", service)
                __service = eval(f"{service}(target_system='{self.target_system}')")
                __service.set_system(self)

                if not __service.load(service_tags):
                    raise Exception("Cam't load the needed libraries")
                
                __service.run()
                    
        return SubSystemController
    
    def load_service(self):
        pass

    def __get_level(self):
        return "<lvl3>" if self.system_level == 2 else "<lvl1>"

    def __check_orders(self, orders:dict):
        if not orders:
            raise Exception("there is no orders from the system")
        return orders

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
        
        return False
    
    def __get_operating_system_level(self) -> int:
        """Identifies the operating system using environment variables and other methods.
        Returns:
            int: The operating system level (e.g., ["Linux", "Windows", "macOS"] => 0, []"Android"] => 2)
        """
        if self.__is_android():
            return 2
            
        # Check for OS using platform information
        if 'android' in self.system_info.release.lower() or 'android' in self.system_info.version.lower():
            return 2
        
        # Call specific OS functions
        if self.__is_windows() or self.__is_macos() or self.__is_linux(): return 0
        
        # raise a system err
        return Exception("System is undefined")