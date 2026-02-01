import requests
import re
from config.vars import URL_ANS


"""
Utiliza um parâmetro int para buscar os trimestres disponíveis dentro do ano desse mesmo parâmetro, retorna uma list contendo os trimestres
"""



def listar_trimestres(ano: int) -> list[str]:
    url = f"{URL_ANS}/{ano}/"

    response = requests.get(url)
    response.raise_for_status()

    html = response.text
    trimestres = set()

    zips = re.findall(r'href="(\dT)\d{4}\.zip"', html)
    trimestres.update(zips)

    trimestres = sorted(trimestres, key=lambda t: int(t[0]), reverse=True)

    return trimestres