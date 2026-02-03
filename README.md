# Ingestão de Demonstrações Contábeis – ANS

Este projeto realiza a ingestão automatizada das Demonstrações Contábeis disponibilizadas pela Agência Nacional de Saúde Suplementar (ANS), identificando dinamicamente os anos, trimestres e arquivos disponíveis no repositório de dados abertos.

O repositório da ANS não disponibiliza uma API estruturada em JSON. Por esse motivo, o projeto realiza a leitura e interpretação do HTML dos diretórios públicos para localizar os arquivos necessários.

---

## Objetivo

Automatizar o processo de:
- Identificação dos anos disponíveis no repositório da ANS;
- Identificação dos trimestres mais recentes;
- Localização dos arquivos ZIP correspondentes;
- Download e extração dos arquivos de dados.

Garantindo que o processo continue funcionando mesmo com a inclusão de novos anos ou trimestres no repositório.

---

## Abordagem adotada

A solução foi construída utilizando Python.

As principais decisões técnicas foram:
- Leitura do HTML do repositório público para identificar diretórios e arquivos disponíveis;
- Uso de expressões regulares para localizar padrões de nomes de arquivos;
- Download dos arquivos de forma incremental (`stream=True`), evitando alto consumo de memória;
- Organização dos dados em pastas separadas para arquivos brutos e extraídos;
- Código modularizado, com cada função responsável por uma única tarefa.

---

## Fluxo de processamento

O pipeline executa as seguintes etapas:

1. Acessa o diretório base de Demonstrações Contábeis da ANS;
2. Identifica os anos disponíveis dinamicamente;
3. Seleciona o ano mais recente;
4. Identifica os trimestres disponíveis desse ano;
5. Seleciona os três trimestres mais recentes;
6. Localiza os arquivos ZIP correspondentes;
7. Realiza o download dos arquivos ZIP;
8. Extrai os arquivos para diretórios individuais por trimestre;
9. Identifica os arquivos CSV extraídos para uso posterior no processamento de dados.

---

## Estrutura do projeto

```text
app/
 ├── config/
 │    └── vars.py
 ├── receber_dados/
 │    ├── listar_anos.py
 │    ├── listar_trimestres.py
 │    ├── listar_zips.py
 │    ├── baixar_zips.py
 │    ├── extrair_zips.py
 │    └── identificar_despesas.py
 └── main.py

data/
 └── raw/
      ├── zips/
      └── extracted/
