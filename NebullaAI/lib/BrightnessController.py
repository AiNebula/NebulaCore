from NebullaAI.lib.OperatingSystemChecker import OperatingSystemChecker
import os
import subprocess

class BrightnessController:
    def __init__(self) -> None:
        # check for libraries
        self.__check_libraries()
        # getting operating system name
        self.operatin_system = OperatingSystemChecker().get_operating_system_name()
        self.max = 100

    def __windows_command(self, amount:int=0) -> bool:
        if subprocess.run([self.nircmd, "setbrightness", f"{amount}"]): return True
        return False

    def __darwin_command(self, action:bool, amount:int) -> bool:
        pass

    def __linux_command(self, action:bool, amount:int) -> bool:
        pass

    def __android_command(self, action:bool, amount:int) -> bool:
        pass
    
    def increase(self, amount:int) -> bool:
        if type(amount) is not int: raise ValueError("The amount must be an Integer between 0 : 100")
        if getattr(self, f"_BrightnessController__{self.operatin_system}_command")(amount): return True
        raise Exception("BrightnessContoller can't increase the brightness.")

    def decrease(self, amount:int) -> bool:
        if type(amount) is not int: raise ValueError("The amount must be an Integer between -0 :100")
        if getattr(self, f"_BrightnessController__{self.operatin_system}_command")(amount): return True
        raise Exception("BrightnessContoller can't decrease the brightness.")

    def __check_libraries(self) -> None:
        """Checking for NirCMD in the system environment path
        """
        libs = ['nircmd']
        for lib in libs:
            if not os.path.isfile(os.path.abspath(f"NebullaAI\\lib\\{lib}.exe")): raise ImportError(f"Failed to load {lib}.")
            self.__setattr__(lib, os.path.abspath(f"NebullaAI\\lib\\{lib}.exe"))