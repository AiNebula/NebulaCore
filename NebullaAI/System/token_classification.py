from transformers import pipeline
import os

class TokenClassifier:
    def __init__(self, model_name:str, version=2, model_dir='models') -> None:
        if self.__check_model(model_dir, version, model_name):
            self.model_name = model_name
            self.version = version
            self.model_dir=model_dir
            self.__load_model()
        else:
            self.__raise_error("Model doesn't exist")
    
    def __load_model(self) -> None:
        self.classifier = pipeline("ner", self.model_path)
    
    def compile(self, prompt:str) -> list:
        return self.classifier(prompt)
    
    def __check_model(self, model_dir, version, model_name) -> bool:
        self.model_path = f"./NebullaAI/{model_dir}/nebulla-ai-v{version}-models/{model_name}"
        return os.path.exists(self.model_path)
    
    def __raise_error(self, err:str) -> str:
        raise Exception(err)