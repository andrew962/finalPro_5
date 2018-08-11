from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)
try:
    bot = ChatBot("Chatterbot",
                              storage_adapter="chatterbot.storage.SQLStorageAdapter",
                              logic_adapters=[
                                  #'chatterbot.logic.MathematicalEvaluation',
                                  'chatterbot.logic.LowConfidenceAdapter',
                                  'chatterbot.logic.BestMatch',
                                  'metro_logic.MyLogicAdapter'
                              ])
    # bot.set_trainer(ChatterBotCorpusTrainer)
    # bot.train("chatterbot.corpus.spanish")
except Exception as e:
    print(e)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    try:
        userText = request.args.get('msg')
    except Exception as e:
        print(e)
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()