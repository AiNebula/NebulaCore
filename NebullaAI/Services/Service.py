class Service:
    """
    Service class is an abstract class that all services are inherted from.
    
    methods : 
        set_system()    -> setting the source system    
    
        load()          -> loading the important configs for the service.
       
        run()           ->  private method that runs the service after desearilzation.
        
        serailze()      -> searilzing the service code for sending to another system.
        
        desearilize()   -> desearilizing the service code for prepearing for running.
    
    """
    def __init__(self) -> None:
        pass

    def set_system(self, system:object) -> None:
        self.system = system
    
    def __get_target_system_num(self, target_system:str):
        return 2 if target_system == '<lvl3>' else 0
    
    def is_same_system(self) -> bool:
        return True if self.system.source_system == self.__get_target_system_num(self.system.target_system) else False

    def load(self):
        pass

    def run(self):
        pass

    def searilze(self):
        pass

    def desearilize(self):
        pass