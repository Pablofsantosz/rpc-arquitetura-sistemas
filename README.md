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

## Experimentos

### Experimento 1 – Chamada remota básica
Ao utilizar a opção de somar números no cliente, a chamada parece uma função normal em Python.  
Porém, na verdade a execução ocorre no servidor. O cliente apenas envia os dados pela rede e recebe o resultado.

**Resposta:**  
A operação foi executada no servidor, não no cliente.

---

### Experimento 2 – Estado remoto
Ao adicionar itens na lista utilizando as opções do cliente, é possível observar que a lista continua armazenando os dados mesmo após várias chamadas.

**Resposta:**  
A lista está armazenada no servidor, pois o estado da aplicação fica no lado remoto e não na memória do cliente.

---

### Experimento 3 – RPC síncrono
Ao executar a chamada demorada (por exemplo 5 segundos), o cliente fica aguardando até o servidor terminar a execução.

**Resposta:**  
O cliente não continua trabalhando enquanto espera. Ele fica bloqueado até receber a resposta do servidor.

---

### Experimento 4 – Falha do servidor
Quando o servidor é interrompido (Ctrl + C) e o cliente tenta executar uma nova operação, ocorre um erro de conexão.

**Resposta:**  
Uma chamada remota pode falhar porque a comunicação depende da rede e do servidor estar ativo.  
Se o servidor estiver desligado ou a conexão for perdida, o cliente não consegue executar o método remoto e ocorre um erro.

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
