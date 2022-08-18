from translate import  Translator
translator = Translator(from_lang="en",to_lang="hi")
sentence = """The President of India, Smt. Droupadi Murmu has sent her greetings to all fellow citizens on the eve of Janmashtami.
In a message, the President has said “On the auspicious occasion of Janmashtami, I extend my warm greetings and best wishes to all the fellow citizens living in India and abroad. Lord Krishna’s life and teachings included the message of well being and virtue. He propagated the concept of “Nishkam Karma” and enlightened the people about the attainment of ultimate truth through the Path of ‘Dharma’. I pray that this festival of Janmashtami inspires us to follow the path of virtue in our thought, words and action”."""
print(sentence)
translation=translator.translate(sentence)

print(translation)

#   \n en English(India)
#   \n gu-IN Gujarati(India)
#   \n hi-IN Hindi(India) 
#   \n kn-IN Kannada(India) 
#   \n kok-IN Konkani(India) 
#   \n mr-IN Marathi(India) 
#   \n pa-IN Punjabi(India) 
#   \n sa-IN Sanskrit(India) 
#   \n ta-IN Tamil(India) 
#   \n te-IN Telugu(India)