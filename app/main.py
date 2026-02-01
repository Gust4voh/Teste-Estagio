from receber_dados.listar_anos import listar_anos_disponiveis
from receber_dados.listar_trimestres import listar_trimestres

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
    ultimos = obter_ultimos_trimestres()
    print("ultimos trimestres encontrados: ")
    for ano, trimestre in ultimos:
        print(f"{trimestre}/{ano}")