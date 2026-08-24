# Contador de Palavras e Caracteres

Um programa simples em Python, feito via terminal, que conta palavras e caracteres em um texto digitado pelo usuário.

## Funcionalidades

- Contagem de **palavras**
- Contagem de **caracteres (com espaços)**
- Contagem de **caracteres (sem espaços)**
- Menu interativo para escolher o tipo de contagem
- Loop contínuo: o programa pergunta se você quer fazer outra contagem antes de encerrar
- Texto convertido para minúsculas antes da análise (`.lower()`)

## Requisitos

- Python 3.6 ou superior

## Como executar

1. Clone o repositório;
2. Execute o script:
   ```
   python contador-de-palavras.py
   ```

## Como usar

Ao iniciar o programa, digite o texto que deseja analisar e escolha uma opção no menu:

```
Digite o texto: Olá, tudo bem?

O que você deseja contar?
1 - Palavras
2 - Caracteres (com espaços)
3 - Caracteres (sem espaços)
4 - Todos
Escolha uma opção (1-5): 4
O texto contém 3 palavras.
Total de caracteres (com espaços): 15
Total de caracteres (sem espaços): 13

Deseja fazer outra contagem? (S/N): n
Encerrando o programa...
```

## Funções principais

| Função | Descrição |
|---|---|
| `contar_palavras(texto)` | Retorna o número de palavras do texto |
| `contar_caracteres(texto, incluir_espacos)` | Retorna o número de caracteres, com ou sem espaços |
| `exibir_menu()` | Exibe as opções de contagem disponíveis |
| `perguntar_novamente()` | Pergunta ao usuário se deseja repetir o processo |

## Possíveis melhorias futuras

- Leitura de texto a partir de arquivos `.txt`;
- Contagem de frequência de cada palavra (`collections.Counter`);
- Remoção de pontuação com expressões regulares;
- Interface gráfica ou versão web.

## Licença

Este projeto está disponível livremente para uso e modificação.

## Autora

Nicole
