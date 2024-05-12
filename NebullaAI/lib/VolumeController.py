from NebullaAI.lib.OperatingSystemChecker import OperatingSystemChecker
import os
import subprocess

class VolumeController:
    def __init__(self) -> None:
        # check for libraries
        self.__check_libraries()
        # getting operating system name
        self.operatin_system = OperatingSystemChecker().get_operating_system_name()
        self.max = 65535

    def __windows_command(self, action:bool=False, amount:int=0, mute=-1) -> bool:
        mute_states = [-1, 0, 1, 2]
        if mute not in mute_states: raise ValueError(f"Can't assign mute_state to {mute}, avilable states are {mute_states}")

        if mute == -1:
            if action:
                subprocess.run([self.nircmd, "changesysvolume", f"{amount}"])
                return True
            subprocess.run([self.nircmd, "changesysvolume", f"-{amount}"])
            return True
        
        subprocess.run([self.nircmd, "mutesysvolume", f"{mute}"])
        return True

    def __darwin_command(self, action:bool, amount:int) -> bool:
        pass

    def __linux_command(self, action:bool, amount:int) -> bool:
        pass

    def __android_command(self, action:bool, amount:int) -> bool:
        pass
    
    def increase(self, amount:int) -> bool:
        if type(amount) is not int: raise ValueError("The amount must be an Integer between -65535 : +65535")
        if getattr(self, f"_VolumeController__{self.operatin_system}_command")(True, amount): return True
        raise Exception("VolumeContoller can't increase the volume.")

    def decrease(self, amount:int) -> bool:
        return getattr(self, f"_VolumeController__{self.operatin_system}_command")(False, amount)
    
    def mute(self) -> bool:
        return getattr(self, f"_VolumeController__{self.operatin_system}_command")(mute=1)
    
    def unmute(self) -> bool:
        return getattr(self, f"_VolumeController__{self.operatin_system}_command")(mute=0)

    def __check_libraries(self) -> None:
        """Checking for NirCMD in the system environment path
        """
        libs = ['nircmd']
        for lib in libs:
            if not os.path.isfile(os.path.abspath(f"NebullaAI\\lib\\{lib}.exe")): raise ImportError(f"Failed to load {lib}.")
            self.__setattr__(lib, os.path.abspath(f"NebullaAI\\lib\\{lib}.exe"))