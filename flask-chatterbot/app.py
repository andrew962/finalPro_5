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
                                  #Desde este punto se estaran aplicando las nuevas logicas creadas
                                  'metro_logic.MyLogicAdapter'
                                  """Esta logica es la que hace la coneccion a la api de metrobus
                                  y tambien valida las diferentes palabras que se introducen
                                  para separarlas del numero de la tarjeta."""
                              ])
    """
    Esta dos lineas comentadas son las que entrenan al chatbot,
    se comentan ya que no siempre se tiene que entrenar el chatbot.
    """
    # bot.set_trainer(ChatterBotCorpusTrainer)
    # bot.train("chatterbot.corpus.spanish")
except Exception as e:
    print(e)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    """
    try: es por si ocurre algun error.
    :except Nos muestra el error de una forma mas detallada
    :var userText: variable que trae lo que le introduscamos.
    :return: retorna la respuesta del bot.
    """
    try:
        userText = request.args.get('msg')
    except Exception as e:
        print(e)
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()