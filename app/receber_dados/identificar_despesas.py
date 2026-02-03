from pathlib import Path

def listar_arquivos_despesas(pastas_extraidas: list[Path]) -> list[Path]:
    arquivos_csv = []

    for pasta in pastas_extraidas:
        for arquivo in pasta.iterdir():
            if arquivo.is_file() and arquivo.suffix == ".csv":
                arquivos_csv.append(arquivo)

    return arquivos_csv
