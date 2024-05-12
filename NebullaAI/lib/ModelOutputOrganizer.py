class ModelOutputOrganizer:
    def __init__(self, model_ouput, auto_run=True) -> None:
        self.model_output = model_ouput
        self.__entities = ['<lvl1>', '<lvl2>', '<lvl3>']
        self.sentences = {}

        if auto_run:
            self.entitize()
            self.add_order()

    def entitize(self):
        for entity in self.model_output:
            if entity['entity'] in self.__entities:
                if not self.__check_none(entity['entity']):
                    self.sentences[entity['entity']]['tokens'].append(entity['word'])
                    continue
                self.sentences[entity['entity']] = { 'tokens' : [entity['word']] }
    
    def add_order(self):
        for lvl, entity in self.sentences.items():
            order_words = []
            for word in entity['tokens']:
                if self.__check_complimant(word):
                    word = word[2:]
                    order_words[-1] += word
                    continue
                order_words.append(word)
            self.sentences[lvl]["order"] = " ".join(order_words)

    def __check_complimant(self, word:str) -> bool:
        if word[:2] == "##": return True
        return False
    
    def __check_none(self, entity:str) -> bool:
        if self.sentences.get(entity) is not None:
            return False
        return True
    