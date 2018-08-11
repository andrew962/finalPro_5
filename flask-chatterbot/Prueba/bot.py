from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

try:
    bot = ChatBot("Chatterbot",
                              storage_adapter="chatterbot.storage.SQLStorageAdapter",
                              logic_adapters=[
                                  'chatterbot.logic.MathematicalEvaluation',
                                  'chatterbot.logic.LowConfidenceAdapter',
                                  'chatterbot.logic.BestMatch',
                                  'metro_logic.MyLogicAdapter',
                                  'wiki_logic.MyWikiLogic'
                              ])
    # bot.set_trainer(ChatterBotCorpusTrainer)
    # bot.train("chatterbot.corpus.spanish")
except Exception as e:
    print(e)

while True:
    try:
        userText = input('-->')
        print(bot.get_response(userText))
    except Exception as e:
        print(e)


