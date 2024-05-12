from NebullaAI.lib.SystemHelper import SystemHelper

class TagClassification(SystemHelper):
    def __init__(self, api_key: str = "AIzaSyCAb5Zjv6crOMNHBcLoCgJ7MkO2Mg_hOj0", temp=0.5, top_p=0.95, top_k=0, max_output_tokens=2048, model_name="gemini-1.0-pro") -> None:
        super().__init__(api_key, temp, top_p, top_k, max_output_tokens, model_name)
        self.set_system()

    def set_system(self) -> None:
        self.convo = self.model.start_chat(history=[
        {
            "role": "user",
            "parts": ["System : tag classifier, the system is a AI assistant that classifiees user input and returns tasks and other details and if it will be outputed in more than one line each line will be in the same format, and the tag classificaion won't get out of (FileServices [file_managment_services [create_file, delete_file, move_file, rename_file], folder_managment_services [create_folder, delete_folder, rename_folder, move_folder, organize_files]], SystemServices[screenshot, audio[increase, decrease, mute], brighntess[increase, decrease], calling], ApplicationServices[launch_application, delete_application], DriverServices[wifi[connect, disconnect, search], bluetooth[search, connect, disconnect]]), and if any task is prompted and it is not belongs to the above classifcation the system return \"This feature isn't implemented yet, do you want to feedback with it ?\".\nUSER : please open a folder \"My Project\" From \"Desktop\" and create a file in it named \"Project1.txt\"."]
        },
        {
            "role": "model",
            "parts": ["ASSISTANT : FileServices, folder_managment_system, create_folder, folder_name:\"My Projects\", location:\"Desktop\"\nASSISTANT : FileServices, file_managment_system, create_file, file_name:\"Project.txt\", location:\"Desktop/My Projects\"\n"]
        }
        ])
    
    def compile(self, prompt) -> list:
        self.convo.send_message(prompt)
        return self.__listify(self.convo.last.text)
    
    def __listify(self, response:str) -> list:
        lines = []
        for line in response.split('\n'):
            if line == '': continue
            lines.append(self.__organize_prompt(line).split(','))
        return lines
    
    def __organize_prompt(self, response:str) -> str:
        if not response.startswith('ASSISTANT'):
            return response
        return response.split(': ')[1]