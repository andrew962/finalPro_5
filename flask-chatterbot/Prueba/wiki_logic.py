from __future__ import unicode_literals
from chatterbot.logic import LogicAdapter
import wikipedia,re


class MyWikiLogic(LogicAdapter):
    def __init__(self, **kwargs):
        super(MyWikiLogic, self).__init__(**kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains.
        """
        palabras = ['buscar','en','wikipedia']
        if all(x in statement.text.split() for x in palabras):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        import requests

        patron=re.compile('\Z')
        texto=patron.split(statement.text)
        print(texto)

        wiki = wikipedia.page(statement)
        content = wiki.content
        if content is not None:
            confidence = 1
        else:
            confidence = 0

        response_statement = Statement('Lo que buscabas \n{}'.format(content))
        response_statement.confidence=confidence

        return response_statement