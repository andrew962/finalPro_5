import re,json,requests
# #
# #
# # metro bus
# text =input('-->')
# #
# # patron=re.compile(r'[0-9]?\D+')
# # palabra = patron.split(text)
# # for x in palabra:
# #     print(x)
#
# patron=re.compile(r'\d\d\d\d\d\d')
# num=patron.search(text)
#
#
#
# url = 'http://panamenio.herokuapp.com/api/com/metrobus/'+num.group()
# response = requests.get(url)
# response.text
# data = json.loads(response.text)
# saldo = str(data['balance'])
# print(saldo)

# """Wikipedia"""
# import wikipedia,re
#
#
# text=input('-->')
#
# patron=re.compile('\Z')
#
# palabra=patron.search(text)
#
# wiki=wikipedia.page(palabra)
#
# content=wiki.content
# if content is not None:
#     print(True)
#     print(content)
# else:
#     print(False)


#
# import re
# numeroTelefonoRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
# mo = numeroTelefonoRegex.search('Mi número de celular es 1534234512')
# if mo:
#     print('Número de teléfono encontrado: ' + mo.group())
# else:
#     print('No se encontró un número de teléfono')


if __name__ == '__main__':
    pass