from NebullaAI.Controllers import SystemController
from NebullaAI.System import PromptBuilder, TokenClassifier, TagClassification
from NebullaAI.lib.ModelOutputOrganizer import ModelOutputOrganizer

# Token classification 
prompt = input("> ")

TC = TokenClassifier("checkpoint-1840")
model_ouput = TC.compile(prompt)

MOO = ModelOutputOrganizer(model_ouput)
sentence = MOO.sentences

PB = PromptBuilder()
Tag_C = TagClassification()

for system, item in sentence.items():
    if system == '<lvl2>': 
        # send to gemnin
        # print("Gemini :", item['order'])
        continue
    pmpt_builder = PB.compile(item['order'])
    item['order'] = pmpt_builder[1]
    item['tags'] = Tag_C.compile(pmpt_builder[1])
    # print("Final Prompt :", pmpt_builder[1])


"""
Handling :
    System Services: 
        Screen Shoot Service,
        Audio Service,
        Brightness Service
    
        
    
Handling : One Level only ( level 1 )

"""

print(sentence)

SC = SystemController(
    sentence
)

    # multi services case
    # {
    #     '<lvl1>': {
    #         'tokens': ['increase', 'to', '100'], 
    #         'order': 'please increase the brightness to 100%',  
    #         'tags': [   ['SystemServices', ' brightness', ' increase', ' brightness_level:100'], 
    #                     ['SystemServices', ' audio', ' unmute']]
    #     }
    # }
    # singke servuce case
    # {
    #     '<lvl1>': {
    #         'tokens': ['increase', 'volume', 'by', '50'], 
    #         'order': 'please increase the volume of "vip" by 50', 
    #         'tags': [['SystemServices', ' audio', ' unmute']]
    #     }
    # }
    # moving file case
    # {
    #     '<lvl1>': {
    #         'tokens': ['move', 'a', 'file'], 
    #         'order': 'move "chapter 2.docx" from "Desktop" to "Documentation" in "Desktop"', 
    #         'tags': [['FileServices', ' file_managment_system', ' move_file', ' file_name:"chapter 2.docx"', ' source_location:"Desktop"', ' destination_location:"D:/Users/Osaaa/Nebulla"']]
    #     }
    # }