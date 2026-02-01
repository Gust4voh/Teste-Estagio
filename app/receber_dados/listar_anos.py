import requests
import re
from config.vars import URL_ANS

"""
Captura todo o html do repositório e armazena em uma variável. Dessa variável, utilizando re busca todos os links disponíveis e retorna uma list[int] contendo os anos
"""


def listar_anos_disponiveis() -> list[int]:
    response = requests.get(URL_ANS)
    response.raise_for_status()

    html = response.text

    anos = re.findall(r'href="(\d{4})/"', html)

    anos = sorted({int(ano) for ano in anos}, reverse=True)

    return anos
