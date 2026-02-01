O repositório de dados abertos ANS não fornece uma API estruturada em JSON, por isso os anos disponíveis são identificados dinamicamente a partir de uma leitura do HTML do diretório de Demonstrações Contábeis.

- Acessa o diretório base,
- Extrai os anos a partir dos links disponíveis,
- Ordena do mais recente para o mais antigo.

De modo que o código continue funcionando mesmo com a inclusão de novos anos no repositório.


