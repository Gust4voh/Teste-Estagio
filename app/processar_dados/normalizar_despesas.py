from datetime import datetime
import csv
import zipfile
from pathlib import Path




def normalizar_registro(reg, ano, trimestre):
    identificador = str(reg.get("REG_ANS", "")).strip()

    try:
        valor = float(
            str(reg.get("VL_SALDO_FINAL", "0"))
            .replace(".", "")
            .replace(",", ".")
        )
    except Exception:
        valor = 0.0

    return {
        "CNPJ": identificador,
        "RazaoSocial": identificador,
        "Trimestre": trimestre,
        "Ano": ano,
        "ValorDespesas": valor
    }


def salvar_csv_e_zip(dados, pasta_saida: Path):
    pasta_saida.mkdir(parents=True, exist_ok=True)

    csv_path = pasta_saida / "consolidado_despesas.csv"
    zip_path = pasta_saida / "consolidado_despesas.zip"

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["CNPJ", "RazaoSocial", "Trimestre", "Ano", "ValorDespesas"]
        )
        writer.writeheader()
        writer.writerows(dados)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname="consolidado_despesas.csv")

    return zip_path
