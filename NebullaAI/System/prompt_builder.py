from NebullaAI.lib.SystemHelper import SystemHelper

class PromptBuilder(SystemHelper):
    def __init__(self, api_key: str = "AIzaSyCjgEJOyJ0FoGvBkHjI-oelcXSenLjVknM", temp=0.5, top_p=0.95, top_k=0, max_output_tokens=2048, model_name="gemini-1.0-pro") -> None:
        super().__init__(api_key, temp, top_p, top_k, max_output_tokens, model_name)
        self.set_system()

    def set_system(self) -> None:
        self.convo = self.model.start_chat(history=[
        {
            "role": "user",
            "parts": ["System : Order generator, the system is a AI assistant that asks for missing details from the users input and asks for the full details and rewrite the user input with the full details for the order, and when it finishs the system returns the full detailed order and the return another prompt EOP.\nUSER : please open a folder for me\n"]
        },
        {
            "role": "model",
            "parts": ["ASSISTANT : what is the name of the folder ?"]
        },
        {
            "role": "user",
            "parts": ["USER : My Projects Folder"]
        },
        {
            "role": "model",
            "parts": ["ASSISTANT : where is the folder is located ?"]
        },
        {
            "role": "user",
            "parts": ["USER : the folder is on the Desktop"]
        },
        {
            "role": "model",
            "parts": ["ASSISTANT : please open \"My Projects\" Folder from \"Desktop\"\nEOP"]
        }
        ])
    
    def compile(self, prompt) -> tuple:
        self.convo.send_message(prompt)
        EOP = self.__EOP(self.convo.last.text)
        if EOP[0]:
            return EOP
        
        print("Nebulla AI :", EOP[1])
        prompt = input("> ")
        return self.compile(prompt)
        
    def __EOP(self, response:str) -> tuple:
        response = response.split('\n')
        if response[-1] == 'EOP' and '?' not in response[0]:
            return (True, self.__organize_prompt(response))
        return (False, self.__organize_prompt(response))
    
    def __organize_prompt(self, response:str) -> str:
        if not response[0].startswith('ASSISTANT'):
            return response[0]
        return response[0].split(': ')[1]