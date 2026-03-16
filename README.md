# Sistema RPC com Python (RPyC)

**Grupo:**  
Pablo Felipe dos Santos

## Descrição
Este projeto implementa um sistema simples de comunicação cliente-servidor utilizando RPC (Remote Procedure Call) com a biblioteca RPyC em Python.

O sistema possui dois arquivos principais:

- servidor.py → responsável por disponibilizar os métodos remotos.
- cliente.py → conecta ao servidor e permite executar operações através de um menu interativo.

O cliente envia requisições ao servidor, que processa os dados e retorna o resultado.

## Métodos Implementados

O servidor possui os seguintes métodos remotos:

somar(a, b)  
Recebe dois números e retorna a soma.

multiplicar(a, b)  
Recebe dois números e retorna o resultado da multiplicação.

contar_caracteres(texto)  
Recebe um texto e retorna a quantidade de caracteres.

adicionar_item(item)  
Adiciona um item em uma lista compartilhada no servidor.

remover_item(item)  
Remove um item da lista compartilhada no servidor.

demorar(segundos)  
Simula uma operação demorada no servidor utilizando sleep.

## Novos Métodos Criados

Para atender ao desafio da atividade foram adicionados novos métodos remotos:

- contar_caracteres(texto) → manipulação de texto  
- multiplicar(a, b) → manipulação de números  
- remover_item(item) → manipulação de lista

## Tratamento de Erros

O cliente possui tratamento de erros para alguns casos:

- Caso o servidor não esteja rodando, o cliente mostra uma mensagem informando que não foi possível conectar.
- Caso a conexão com o servidor seja perdida durante a execução, o cliente informa que houve falha na rede.

## Como Executar o Projeto

1. Instalar a biblioteca necessária

pip install rpyc

2. Executar o servidor

python servidor.py

O servidor será iniciado na porta 18861.

3. Executar o cliente

Em outro terminal execute:

python cliente.py

O cliente irá se conectar ao servidor e mostrar um menu com as opções disponíveis.

## Estrutura do Projeto

rpc-python/
│
├── servidor.py
├── cliente.py
└── README.md

## Conclusão

Com essa prática foi possível entender o funcionamento de um sistema RPC em Python utilizando a biblioteca RPyC, permitindo que um cliente execute métodos que estão sendo processados no servidor. Também foram implementados novos métodos e tratamento de erros para tornar o sistema mais completo.