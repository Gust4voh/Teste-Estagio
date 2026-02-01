from receber_dados.listar_anos import listar_anos_disponiveis
from receber_dados.listar_trimestres import listar_trimestres
from receber_dados.listar_zips import listar_zips_trimestre
from receber_dados.baixar_zips import baixar_zips
from config.vars import PASTA_ZIPS

def obter_ultimos_trimestres(quantidade=3):
    resultados = []

    anos = listar_anos_disponiveis()

    for ano in anos:
        trimestres = listar_trimestres(ano)

        for trimestre in trimestres:
            resultados.append((ano, trimestre))

            if len(resultados) == quantidade:
                return resultados
            
    return resultados

if __name__ == "__main__":

    urls = listar_zips_trimestre(2025, "3T")

    baixar_zips(
        urls,
        PASTA_ZIPS
    )

