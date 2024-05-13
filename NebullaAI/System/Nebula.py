from NebullaAI.lib.SystemHelper import SystemHelper

class Nebula(SystemHelper):
    def __init__(self, api_key: str = "AIzaSyCAb5Zjv6crOMNHBcLoCgJ7MkO2Mg_hOj0", temp=1, top_p=0.95, top_k=0, max_output_tokens=4096, model_name="gemini-1.5-pro-latest") -> None:
        super().__init__(api_key, temp, top_p, top_k, max_output_tokens, model_name)
        self.set_system()

    def set_system(self) -> None:
        self.convo = self.model.start_chat(history=[
        {
            "role": "user",
            "parts": ["System : You're Nebula the first ecosystem-based AI in the world, created by Nebula team, you're a High level AI system that involves with user in conversation and detect what the prompt should actually means by understanding the context and when you asked about any thing about the system control you should tell about your abilities, you've three levels system, 1st level is Primary System which contains any related Computer orders in the prompt, 2nd system in LLM system the responsible for Creative Text Generation and Online searching for things, 3rd System is Terminal System which contains any phone related orders in the prompt, you main purpose is to talk with the user as friend and answers his questions about the system and if the user sends a prompt that runs only on one of the 1st or 3rd systems like (opening a folder, createing a file, connection to wifi, taking a screenshot, etc.) or a prompt that contains a compination of the three systen you return an answer contains only number 1."]
        }
        ])
    
    def compile(self, prompt) -> str:
        self.convo.send_message(prompt)
        if self.__is_true(self.convo.last.text):
            return self.convo.history[-2].parts[0].text
        print(f"Nebula : {self.convo.last.text} \n")
        prompt = input('> ')
        return self.compile(prompt)
    
    def compile_ui(self, prompt) -> str|dict:
        response = self.convo.send_message(prompt)
        if self.__is_true(self.convo.last.text):
            return self.convo.history[-2].parts[0].text
        return {"response": self.convo.last.text, "response_feedback": response.prompt_feedback}
    
    def __is_true(self, response:str):
        try:
            if int(response) == 1:
                return True
            return False
        except ValueError as e:
            return False