from NebullaAI.Services import Service
from NebullaAI.lib.NameCleaner import remove_spaces_quotes
from NebullaAI.lib.VolumeController import VolumeController

class audioService(Service):
    def __init__(self, attrs:list) -> None:
        super().__init__()
        self.attrs = attrs
        self.un_parameterized_actions = ['mute', 'unmute']
    
    def __attrs_organize(self, attr_name):
        if '%' in attr_name or attr_name in ['percentage']:
            return 'percentage'
        elif attr_name in ['value', 'increase_by', 'increased_by', 'by', 'volume', 'decrease_by', 'decreased_by', 'volume_level', 'audio_value', 'level']:
            return 'value'

    def __attrs(self) -> None:
        if hasattr(self, 'percentage'): 
            self.value = int((self.percentage/100) * self.vc.max)
            return
        if not hasattr(self, 'value'): raise Exception("you need to specify a value, or percentage")
        self.value = int((self.value/100) * self.vc.max)


    def load(self) -> bool:
        for attr in self.attrs:
            try:
                attr_name, attr_value = attr.split(":")
                try:
                    setattr(self, self.__attrs_organize(remove_spaces_quotes(attr_name)), int(remove_spaces_quotes(attr_value)))
                except TypeError as e:
                    pass
            except ValueError as e:
                self.action = remove_spaces_quotes(remove_spaces_quotes(attr))
            
            if self.action in self.un_parameterized_actions: break
        
        self.vc = VolumeController()

        if self.action not in self.un_parameterized_actions: self.__attrs()

        if self.is_same_system():
            # load the needed module based on the system level
            if self.system.source_system == 0:
                # getting increase and decrease first
                if self.action not in self.un_parameterized_actions: 
                    self.command = f"self.vc.{self.action}({self.value})"
                    return True
                self.command = f"self.vc.{self.action}()"
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
            # increase, decrease, mute or unmute
            if eval(self.command):
                return True
            return False
        # lvl3
        elif self.system == 2:
            return True
                
        return False

    def searilze(self):
        return super().searilze()
    
    def desearilize(self):
        return super().desearilize()