from translate import  Translator
from fastapi import FastAPI
from pydantic import BaseModel

class translateClass(BaseModel):
    sentence:str
    toLang:str


app = FastAPI()

@app.post("/home/")
async def getRecommendation(translation:translateClass):
    translator = Translator(from_lang="en",to_lang=translation.toLang)

    translation=translator.translate(translation.sentence)
        
    return [{
        "Translation":translation
    }]
