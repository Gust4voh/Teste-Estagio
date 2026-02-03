from pathlib import Path

from config.vars import PASTA_ZIPS, PASTA_EXTRAIDOS

from receber_dados.listar_anos import listar_anos_disponiveis
from receber_dados.listar_trimestres import listar_trimestres
from receber_dados.listar_zips import listar_zips_trimestre
from receber_dados.baixar_zips import baixar_zips
from receber_dados.extrair_zips import extrair_zips
from receber_dados.identificar_despesas import listar_arquivos_despesas

from processar_dados.filtrar_despesas import filtrar_despesas_eventos
from processar_dados.normalizar_despesas import (
    normalizar_registro,
    salvar_csv_e_zip
)


def main():
    anos = listar_anos_disponiveis()
    if not anos:
        print("Nenhum ano disponível.")
        return

    ano_mais_recente = anos[0]

    trimestres = listar_trimestres(ano_mais_recente)
    if not trimestres:
        print("Nenhum trimestre disponível.")
        return

    ultimos_trimestres = trimestres[:3]

    urls_zips = []
    for trimestre in ultimos_trimestres:
        urls_zips.extend(
            listar_zips_trimestre(ano_mais_recente, trimestre)
        )

    if not urls_zips:
        print("Nenhum ZIP encontrado.")
        return

    arquivos_zip = baixar_zips(urls_zips, PASTA_ZIPS)

    pastas_extraidas = extrair_zips(arquivos_zip, PASTA_EXTRAIDOS)

    arquivos_despesas = listar_arquivos_despesas(pastas_extraidas)

    print("\nArquivos encontrados:")
    for a in arquivos_despesas:
        print(a)

    csvs = []
    for pasta in pastas_extraidas:
        csvs.extend(pasta.glob("*.csv"))

    registros = filtrar_despesas_eventos(csvs)

    print(f"\nRegistros brutos encontrados: {len(registros)}")

    dados_finais = []

    for pasta in pastas_extraidas:
        nome_pasta = pasta.name
        trimestre = nome_pasta[:2]
        ano = int(nome_pasta[2:])

        for reg in registros:
            dados_finais.append(
                normalizar_registro(
                    reg,
                    ano=ano,
                    trimestre=trimestre
                )
            )

    zip_final = salvar_csv_e_zip(
        dados_finais,
        Path("data/output")
    )

    print(f"\nArquivo final gerado em: {zip_final}")


if __name__ == "__main__":
    main()
