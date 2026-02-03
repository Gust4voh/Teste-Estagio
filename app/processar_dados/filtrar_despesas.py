import csv
from pathlib import Path


"""
recebe uma lista contendo o caminho dos csvs
"""


def filtrar_despesas_eventos(csvs: list[Path]) -> list[dict]:
    registros_filtrados = []

    for csv_path in csvs:
        with open(csv_path, newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(
                arquivo,
                delimiter=";"
            )

            for linha in leitor:
                descricao = linha.get("DESCRICAO", "")

                if "Eventos / Sinistros" in descricao:
                    registros_filtrados.append(linha)

    return registros_filtrados