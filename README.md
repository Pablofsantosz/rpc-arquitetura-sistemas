# Sistema RPC com Python (RPyC)

**Grupo:** Pablo Felipe dos Santos

## Descrição
Este projeto implementa um sistema simples de comunicação cliente-servidor utilizando RPC (Remote Procedure Call) com a biblioteca RPyC em Python.

O sistema possui dois arquivos principais:

- `servidor.py` → responsável por disponibilizar os métodos remotos.
- `cliente.py` → conecta ao servidor e permite executar operações através de um menu interativo.

O cliente envia requisições ao servidor, que processa os dados e retorna o resultado.

## Métodos Implementados

O servidor possui os seguintes métodos remotos:

- **`somar(a, b)`** Recebe dois números e retorna a soma.

- **`multiplicar(a, b)`** Recebe dois números e retorna o resultado da multiplicação.

- **`contar_caracteres(texto)`** Recebe um texto e retorna a quantidade de caracteres.

- **`adicionar_item(item)`** Adiciona um item em uma lista compartilhada no servidor.

- **`remover_item(item)`** Remove um item da lista compartilhada no servidor.

- **`demorar(segundos)`** Simula uma operação demorada no servidor utilizando sleep.

## Novos Métodos Criados

Para atender ao desafio da atividade foram adicionados novos métodos remotos:

- `contar_caracteres(texto)` → manipulação de texto  
- `multiplicar(a, b)` → manipulação de números  
- `remover_item(item)` → manipulação de lista

## Tratamento de Erros

O cliente possui tratamento de erros para alguns casos:

- Caso o servidor não esteja rodando, o cliente mostra uma mensagem informando que não foi possível conectar.
- Caso a conexão com o servidor seja perdida durante a execução, o cliente informa que houve falha na rede.

### Como Executar o Projeto

### Passos para Execução

1. **Instalar a biblioteca necessária**
    ```bash
    pip install rpyc
    ```

2.  **Executar o servidor**
    ```bash
    python servidor.py
    ```

3.  **Executar o cliente**
    ```bash
    python cliente.py
    ```
