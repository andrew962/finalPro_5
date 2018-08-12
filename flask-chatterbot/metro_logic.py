from __future__ import unicode_literals
from chatterbot.logic import LogicAdapter
import re

class MyLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(MyLogicAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains.
        """
        """
        :var patron: es como el validador que buscara dentro de la oracion los numeros.
        :var self.num: donde se guardan los numeros despues de hacer la busqueda con los parametros
        que le pasamos por patron.
        """
        patron = re.compile(r'\d\d\d\d\d\d\d\d')
        self.num = patron.search(statement.text)

        """
        :list words: son las palabras claves que el chatbot utilizara para detectar
        que tiene que hacer una busqueda de saldo de metro bus.
        """
        words = ['mi','saldo']
        """
        if all(x in statement.text.split() for x in words):
        hace la busqueda palabra por palabra validando cada una
        :return True: si encuentra alguna de las dos palabras.
        """
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        import requests,json

        #api metro bus
        """
        :var url: api de metro bus
        :self.num.group(): aqui hago referecia al numero obtenido de la busqueda que se hizo mas arriba
        por medio de self.num = patron.search(statement.text).
        :var response: se hace el llamado de la api para obtener los valores.
        """
        url ='http://panamenio.herokuapp.com/api/com/metrobus/'+self.num.group()
        response = requests.get(url)
        response.text
        # Let's base the confidence value on if the request was successful
        """
        if response.status_code == 200: valida que la coneccion con la api fue exitosa, si cumple la condicion
        la confianza para a 1 para que el bot lo agrege a la base de datos y pueda se impreso.
        """
        if response.status_code == 200:
            confidence = 1
        else:
            confidence = 0

        data = json.loads(response.text)
        saldo = str(data['balance'])
        """
        :response_statement = Statement('Tu saldo es {}'.format(saldo)): de esta manera es que el bot nos lo estuviera
        mostrando en pantalla.
        """
        response_statement = Statement('Tu saldo es {}'.format(saldo))
        response_statement.confidence=confidence

        return response_statement
