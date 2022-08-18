from translate import  Translator
from fastapi import FastAPI
# from pydantic import BaseModel

# class translateClass(BaseModel):
#     sentence:str


app = FastAPI()

@app.post("/home")
def getRecommendation():
    sentence="""Goa and Dadra & Nagar Haveli and Daman & Diu (D&NH and D&D) becomes the first ‘Har Ghar Jal’ certified State and UT in the country respectively, where people from all the villages have declared their village as ‘Har Ghar Jal’ through a resolution passed by Gram Sabha, certifying that all households in the villages have access to safe drinking water through taps, ensuring that ‘No One is Left Out’.  All 2.63 lakh rural households of Goa & 85,156 of Dadra & Nagar Haveli and Daman & Diu have access to potable water through tap connection.

Jal Jeevan Mission is a flagship programme of Government of India which was announced from the ramparts of Red Fort by visionary Prime Minister on August 15, 2019. The mission aims to make provision of potable tap water supply in adequate quantity, of prescribed quality and on regular & long-term basis to every rural household of the country by 2024. The program is implemented by Government of India in partnership with States/UTs.
Despite various disruptions and challenges faced during COVID-19 pandemic, the consistent efforts by Panchayat representatives, Pani Samitis, District and State/UT officials of Goa and D&NH and D&D have led tothis achievement.All schools, anganwadi centres, public institutions including Gram Panchayat buildings, healthcare centres, community centres, ashramshalas, and other government offices have now access to potable water through tap connection.
The process of certification has been detailed out in the Margdarshika of Jal Jeevan Mission according to which first of all, the field engineer submits a completion certificate regarding water supply scheme to the Panchayat during Gram Sabha meeting. The villages confirm through a resolution of the Gram Sabha, that every household is getting regular supply of water of prescribed quality and not a single household is left out. They also confirm that all schools, anganwadi centers and other public institutions also getting tap water.
Village Water and Sanitation Committee (VWSC) or paani samiti has been constituted in all the 378 villages of Goa and 96 villages of D&NH and D&D. VWSC is responsible for operation, maintenance and repair of water supply infrastructure developed under ‘Har Ghar Jal’ programme. This sub-committee of Gram Panchayat also has the responsibility to collect user charge which will be deposited in the bank account and shall be used to pay honorarium of the pump operator and carry out minor repair work from time-to-time.

Water Quality is an important aspect of the mission and to ensure the same, at least five women in every village are trained to carry out water testing. Today more than 10 lakh women in the country have been trained to use Field Test Kits (FTKs) for testing the quality of water supplied in rural households. More than 57 lakh water samples have been tested by these women using Field Testing Kits (FTKs)

Following Prime Minister Shri Narendra Modi’s vision of “Sabka Saath, Sabka Vikas, Sabka Vishwas aur Sabka Prayas”, more than 52% rural households in the country are now connected with tap water which was only 17% at the time of launch of this transformational mission on August 15, 2019."""
    translator = Translator(from_lang="en",to_lang="hi")

    translation=translator.translate(sentence)
        
    return [{
        "Translation":translation
    }]
