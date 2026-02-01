import requests
import re
from config.vars import URL_ANS


"""
Recebe um ano e um trimestre, então lista os arquivos .zip presentes
"""


def listar_zips_trimestre(ano: int, trimestre: str) -> list[str]:
    zips_encontrados = []

    url_ano = f"{URL_ANS.rstrip('/')}/{ano}/"
    response = requests.get(url_ano)
    response.raise_for_status()

    html = response.text
    zips = re.findall(r'href="(\dT\d{4}\.zip)"', html)
    zips = [z for z in zips if z.startswith(trimestre)]

    for zip_nome in zips:
        zips_encontrados.append(f"{url_ano}{zip_nome}")

    return zips_encontrados
