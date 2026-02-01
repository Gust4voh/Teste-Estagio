import requests
from pathlib import Path


"""
Recebe como parametro a url do arquivo e a pasta de destino
"""

def baixar_zips(urls: list[str], pasta_destino: str) -> list[Path]:
    arquivos_baixados = []

    pasta = Path(pasta_destino)
    pasta.mkdir(parents=True, exist_ok=True)

    for url in urls:
        nome_arquivo = url.split("/")[-1]
        caminho_arquivo = pasta / nome_arquivo

        if caminho_arquivo.exists():
            arquivos_baixados.append(caminho_arquivo)
            continue
        
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(caminho_arquivo, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        arquivos_baixados.append(caminho_arquivo)

    return arquivos_baixados