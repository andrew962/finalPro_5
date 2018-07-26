from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import threading,requests,json,sys

app = Flask(__name__)

floppy = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
floppy.set_trainer(ChatterBotCorpusTrainer)
floppy.train("chatterbot.corpus.spanish")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(floppy.get_response(userText))


if __name__ == "__main__":
    app.run()
