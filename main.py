output_of_model = [{'entity': '<lvl3>',
  'score': 0.5380187,
  'index': 1,
  'word': 'take',
  'start': 0,
  'end': 4},
 {'entity': '<lvl3>',
  'score': 0.5150598,
  'index': 2,
  'word': 'a',
  'start': 5,
  'end': 6},
 {'entity': '<lvl3>',
  'score': 0.397075,
  'index': 3,
  'word': 'screens',
  'start': 7,
  'end': 14},
 {'entity': '<lvl3>',
  'score': 0.49737096,
  'index': 4,
  'word': '##hot',
  'start': 14,
  'end': 17},
 {'entity': '<lvl3>',
  'score': 0.48813468,
  'index': 5,
  'word': 'from',
  'start': 18,
  'end': 22},
 {'entity': '<lvl3>',
  'score': 0.51509833,
  'index': 6,
  'word': 'my',
  'start': 23,
  'end': 25},
 {'entity': '<lvl3>',
  'score': 0.5034389,
  'index': 7,
  'word': 'phone',
  'start': 26,
  'end': 31},
 {'entity': '<lvl1>',
  'score': 0.51780784,
  'index': 8,
  'word': 'and',
  'start': 32,
  'end': 35},
 {'entity': '<lvl1>',
  'score': 0.49261594,
  'index': 9,
  'word': 'pass',
  'start': 36,
  'end': 40},
 {'entity': '<lvl1>',
  'score': 0.44963938,
  'index': 10,
  'word': 'it',
  'start': 41,
  'end': 43},
 {'entity': '<lvl1>',
  'score': 0.505248,
  'index': 11,
  'word': 'to',
  'start': 44,
  'end': 46},
 {'entity': '<lvl1>',
  'score': 0.48746106,
  'index': 12,
  'word': 'my',
  'start': 47,
  'end': 49},
 {'entity': '<lvl1>',
  'score': 0.4914846,
  'index': 13,
  'word': 'desktop',
  'start': 50,
  'end': 57},
 {'entity': '<lvl1>',
  'score': 0.49897465,
  'index': 14,
  'word': 'in',
  'start': 58,
  'end': 60},
 {'entity': '<lvl1>',
  'score': 0.45143119,
  'index': 15,
  'word': 'computer',
  'start': 61,
  'end': 69}]


class Module:
    def __init__(self, name, system) -> None:
        self.system = system
        self.name = name
    
    def load(self) -> bool:
        # loading the child module from the load function
        try:
            self.module = eval(f"{self.name}Module('{self.system}')")
            self.module.load()
            return True
        except NameError as e:
            print(f"the {self.name} functionality isn't emplimented yet.")
            return False
    
    def run(self):
        # running the child module from the run function
        self.module.run()

class screenshotModule(Module):
    def __init__(self, system) -> None:
        self.system = system
    
    def load(self):
        # important configs for loading
        from mss import mss
        self.mss = mss
        # print(f"loading {self} for {self.system}")

    def run(self):
        # running the module passed on the system
        # the _screenshotModule__ -> will be replaced with a generalized code to be added
        # to the parent (Module) class
        _run = getattr(self, f"_screenshotModule__{self.system[1:-1]}_run")
        _run()

    def __lvl1_run(self):
        # running module pased on lvl1 system
        with self.mss() as sct:
            # capture the screenshot
            screenshot = sct.shot(output = "test.png")

    def __lvl3_run(self):
        # running module passed on lvl3 system
        with self.mss() as sct:
            # capture the screenshot
            screenshot = sct.shot(output = "test.png")
        # print(f"running the __lvl3_run() function from run")

class shareModule(Module):
    def __init__(self, system) -> None:
        self.system = system
    
    def load(self):
        # important configs for loading
        print(f"loading {self} for {self.system}")

    def run(self):
        # running the module passed on the system
        # the _screenshotModule__ -> will be replaced with a generalized code to be added
        # to the parent (Module) class
        _run = getattr(self, f"_shareModule__{self.system[1:-1]}_run")
        _run()

    def __lvl1_run(self):
        # running module pased on lvl1 system
        
        # searilzie
        # send to another system
        # or recieve from antoher service and desearilze
        
        print(f"running the __lvl1_run() function from run")
    
    def __lvl3_run(self):
        # running module passed on lvl3 system
        
        # searilze
        # send to another service
        # or recieve from another service and desearilze
        
        print(f"running the __lvl3_run() function from run")

class entity:
    def __init__(self) -> None:
        self.name:str = ""
    
    def load_module(self, name):
        module = Module(name, self)
        if not module.load(): return False
        return module

    def tags(self, tags:list) -> bool:
        if tags == []:
            return False
        self.tags = tags
        for tag in self.tags:
            call = self.call_sub_entity(tag)
            if not call:
                return False
        return True
    
    def call_sub_entity(self, tag:str):
        sub_entity(tag, self).call()

    def __repr__(self) -> str:
        return self.name

class sub_entity(entity):
    def __init__(self, tag, system) -> None:
        super().__init__()
        self.name = tag
        self.system = system
    
    def call(self):
        # loading submodule based on system
        module = self.system.load_module(self.name)
        # running
        if not module: return False
        module.run()
        return True

class lvl1(entity):
    def __init__(self) -> None:
        super().__init__()
        self.name = "<lvl1>"

    def __repr__(self) -> str:
        return super().__repr__()

class lvl2(entity):
    def __init__(self) -> None:
        super().__init__()
        self.name = "<lvl2>"

    def __repr__(self) -> str:
        return super().__repr__()

class lvl3(entity):
    def __init__(self) -> None:
        super().__init__()
        self.name = "<lvl3>"

    def __repr__(self) -> str:
        return super().__repr__()

sentence = {}
for entity in output_of_model:
    _entity = entity['entity']
    if _entity == '<lvl1>':
        if sentence.get('<lvl1>') is not None:
            sentence['<lvl1>']['tokens'].append(entity['word'])
            continue
        sentence['<lvl1>'] = { 'tokens' : [entity['word']] }
    elif _entity == '<lvl2>':
        if sentence.get('<lvl2>') is not None:
            sentence['<lvl2>']['tokens'].append(entity['word'])
            continue
        sentence['<lvl2>'] = { 'tokens' : [entity['word']] }
    elif _entity == '<lvl3>':
        if sentence.get('<lvl3>') is not None:
            sentence['<lvl3>']['tokens'].append(entity['word'])
            continue
        sentence['<lvl3>'] = { 'tokens' : [entity['word']] }

for lvl, info in sentence.items():
    if info['tokens'] == []: 
        sentence[lvl]['order'] = ""
        continue
    text_sentenct = []
    for word in info['tokens']:
        if word[:2] == "##":
            word = word[2:]
            text_sentenct[-1] += word
            continue
        text_sentenct.append(word)
    sentence[lvl]["order"] = " ".join(text_sentenct)

# orderize the order
sentence['<lvl1>']['tags'] = ['share']
sentence['<lvl3>']['tags'] = ['screenshot']

# get tags from lvls
for lvl, item in sentence.items():
    if lvl == '<lvl1>':
        lvl1().tags(item['tags'])
    elif lvl == '<lvl2>':
        lvl2().tags(item['tags'])
    elif lvl == '<lvl3>':
        lvl3().tags(item['tags'])