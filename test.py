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

print(sentence)