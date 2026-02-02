from config.vars import PASTA_ZIPS, PASTA_EXTRAIDOS

from receber_dados.listar_anos import listar_anos_disponiveis
from receber_dados.listar_trimestres import listar_trimestres
from receber_dados.listar_zips import listar_zips_trimestre
from receber_dados.baixar_zips import baixar_zips
from receber_dados.extrair_zips import extrair_zips


def main():
    anos = listar_anos_disponiveis()

    if not anos:
        return

    ano_mais_recente = anos[0]

    trimestres = listar_trimestres(ano_mais_recente)

    if not trimestres:
        return

    ultimos_trimestres = trimestres[:3]

    urls_zips = []
    for trimestre in ultimos_trimestres:
        urls = listar_zips_trimestre(ano_mais_recente, trimestre)
        urls_zips.extend(urls)

    if not urls_zips:
        return

    arquivos_zip = baixar_zips(urls_zips, PASTA_ZIPS)

    extrair_zips(arquivos_zip, PASTA_EXTRAIDOS)


if __name__ == "__main__":
    main()
