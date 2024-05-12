from NebullaAI.Services import Service
from NebullaAI.lib.NameCleaner import remove_spaces_quotes
from NebullaAI.lib.BathBuilder import BathBuilder
import datetime

class screenshotService(Service):
    def __init__(self, attrs:list) -> None:
        super().__init__()
        self.attrs = attrs
    
    def __attrs_organize(self, attr_name):
        if 'location' in attr_name:
            return 'location'
        elif attr_name in ['file_name', 'filename', 'save_as', 'screenshot_name']:
            return 'filename'

    def __attrs(self) -> None:
        if not hasattr(self, 'location'):
            self.location = "Desktop"

        if not hasattr(self, 'filename'):
            self.filename = f"Screenshot-{datetime.now()}.png"

    def load(self) -> bool:
        print("attrs:", self.attrs)
        for attr in self.attrs:
            attr_name, attr_value = attr.split(":")
            try:
                setattr(self, self.__attrs_organize(remove_spaces_quotes(attr_name)), remove_spaces_quotes(attr_value))
            except TypeError as e:
                pass
        
            
        self.__attrs()

        if self.is_same_system():
            # load the needed module based on the system level
            if self.system.source_system == 0:
                from mss import mss
                self.mss = mss
                return True
            elif self.system.source_system == 2:
                # needed prepreation for mobile
                # return True
                pass
        else:
            # searilzed for sharing
            # return True
            pass

        return False

    def run(self) -> bool:
        # lvl1
        if self.system.source_system == 0:
            bb = BathBuilder(self.system)
            path = bb.build(self.location)
            with self.mss() as sct:
                sct.shot(output = f"{path}\\{bb.filename_extention(self.filename, '.png')}")
            return True
        elif self.system == 2:
            print("code for the lvl3 service")
            return True
        
        return False

    def searilze(self):
        return super().searilze()
    
    def desearilize(self):
        return super().desearilize()