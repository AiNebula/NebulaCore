from NebullaAI.Services import Service
from NebullaAI.lib.NameCleaner import remove_spaces_quotes, remove_surrounding_spaces
from NebullaAI.lib.FileController import FileController
import datetime

class file_managment_systemService(Service):
    def __init__(self, attrs:list) -> None:
        super().__init__()
        self.attrs = attrs
    
    def load(self) -> bool:
        for attr in self.attrs:
            try:
                attr_name, attr_value = attr[:attr.find(':')], attr[attr.find(':') + 1:]
                print(attr_name, attr_value)
                setattr(self, self.__attrs_organize(remove_spaces_quotes(attr_name)), remove_surrounding_spaces(attr_value))
            except TypeError as e:
                self.action = remove_spaces_quotes(attr)
        
        self.fc = FileController()
    
        self.__attrs()

        if self.is_same_system():
            # load the needed modules based on the system level
            if self.system.source_system == 0:
                # create the command

                # if creating, deleting
                if self.action not in ["move_file", "rename_file"]: 
                    self.command = f"self.fc.{self.action}('{self.filename}', '{self.location}', content='{self.content}')"
                    return True
                
                # if moving, renaming a file is the action
                self.command = f"self.fc.{self.action}('{self.filename}', '{self.location}', '{self.destination}')"

                return True
            elif self.system.source_system == 2:
                # needed preperations for mobile
                # return true
                pass
        else:
            # searilze for sharing
            # return True
            pass

        return False

    def run(self) -> bool:
        # lvl1
        if self.system.source_system == 0:
            # create, delete, move
            if eval(self.command):
                return True
            return False
        elif self.system == 2:
            return True
    
    def searilze(self):
        return super().searilze()
    
    def desearilize(self):
        return super().desearilize()
    
    def __attrs(self) -> None:
        if not hasattr(self, 'location') or 'current' in self.location.lower():
            self.location = 'Desktop'
        
        if not hasattr(self, 'filename'):
            self.filename = f"file-create-by-nebullaai-{datetime.now()}"

        if not hasattr(self, 'content'):
            self.content = ""
        
        if not hasattr(self, "destination"):
            self.destination = ""
        
    def __attrs_organize(self, attr_name) -> str:
        if 'location' == attr_name or 'source' in attr_name or attr_name in ['location_from', 'origin', 'from']:
            return 'location'
        elif attr_name in ['file_name', 'filename', 'save_as', 'name']:
            return 'filename'
        elif attr_name in ['content']:
            return 'content'
        elif 'destination' in attr_name or attr_name in ['location_to', 'to']:
            return "destination"