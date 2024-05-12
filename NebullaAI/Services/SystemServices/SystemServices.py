from .SubServices import screenshotService, audioService, brightnessService

class SystemServices:
    def __init__(self, target_system:str) -> None:
        self.target_system = target_system

    def set_system(self, system) -> None:
        self.system = system

    def load(self, service_tags:list) -> bool:
        # load service
        print("loading : ", service_tags[0])
        self.__sub_service = eval(f"{service_tags[0]}Service({service_tags[1:]})")
        self.__sub_service.set_system(self.system)
        return self.__sub_service.load()

    def run(self) -> None:
        if not self.__sub_service.run():
            raise Exception("Can't run the Service")