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
        aqui abajo dentro del parrafo que se introdujo se busca una serie de numeros de 6 caracteres( patron = re.compile(r'\d\d\d\d\d\d\d\d') )
        """
        patron = re.compile(r'\d\d\d\d\d\d\d\d')
        self.num = patron.search(statement.text)

        words = ['mi','saldo']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        import requests,json

        url ='http://panamenio.herokuapp.com/api/com/metrobus/'+self.num.group()
        response = requests.get(url)
        response.text
        # Let's base the confidence value on if the request was successful
        if response.status_code == 200:
            confidence = 1
        else:
            confidence = 0

        data = json.loads(response.text)
        saldo = str(data['balance'])
        response_statement = Statement('saldo '+saldo)
        response_statement.confidence

        return response_statement
