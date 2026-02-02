from pathlib import Path
from zipfile import ZipFile

def extrair_zips(arquivos_zip: list[Path], pasta_destino: str) -> list[Path]:
    caminhos_extraidos = []

    pasta = Path(pasta_destino)
    pasta.mkdir(parents=True, exist_ok=True)

    for zip_path in arquivos_zip:
        pasta_zip = pasta / zip_path.stem

        if pasta_zip.exists():
            caminhos_extraidos.append(pasta_zip)
            continue

        with ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(pasta_zip)

        caminhos_extraidos.append(pasta_zip)

    return caminhos_extraidos
