import google.generativeai as genai

class SystemHelper:
    def __init__(self, api_key:str = "AIzaSyCjgEJOyJ0FoGvBkHjI-oelcXSenLjVknM",
                 temp=0.5, top_p=0.95, top_k=0, max_output_tokens=2048,
                 model_name="gemini-1.0-pro") -> None:
        genai.configure(api_key=api_key)
        self.configure(temp, top_p, top_k, max_output_tokens)
        self.model(model_name)
    
    def configure(self, temp:int, top_p:float, top_k:int, max_output_tokens:int) -> None:
        # Set up the model
        
        self.generation_config = {
        "temperature": temp,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
        }

        self.safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
        ]
    
    def model(self, model_name:str) -> None:
        self.model = genai.GenerativeModel(model_name=model_name,
                                    generation_config=self.generation_config,
                                    safety_settings=self.safety_settings)
    
    def set_system(self) -> None:
        pass

    def compile(self) -> None:
        pass
    
    