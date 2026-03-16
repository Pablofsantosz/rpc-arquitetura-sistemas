import rpyc
import sys

def main():
    try:
        conn = rpyc.connect("localhost", 18861)
        print("Conectado ao servidor com sucesso!")
    except ConnectionRefusedError:
        print("Erro Crítico: Não foi possível conectar ao servidor. Verifique se ele está rodando.")
        sys.exit(1)

    while True:
        print("\nMenu RPC ")
        print("1. Somar dois números")
        print("2. Adicionar item à lista remota")
        print("3. Chamada demorada  (5 segundos)")
        print("4. Multiplicar dois números (Novo)")
        print("5. Contar caracteres (Novo)")
        print("6. Remover item da lista (Novo)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                print("Informe o primeiro número:")
                num1 = float(input())
                print("Informe o segundo número:")
                num2 = float(input())
                resultado = conn.root.somar(num1, num2)
                
                print(f"Resultado da soma ({num1} + {num2}): {resultado}")
            elif opcao == '2':
                item = input("Digite o item para adicionar: ")
                itens = conn.root.adicionar_item(item)
                print(f"Estado atual da lista: {itens}")
                
            elif opcao == '3':
                print("Iniciando chamada demorada aguarde.")
                resultado = conn.root.demorar(5) 
                print(f"Resultado: {resultado}")
                
            elif opcao == '4':
                print("Informe o primeiro número:")
                num1 = float(input())
                print("Informe o segundo número:")
                num2 = float(input())
                resultado = conn.root.somar(num1, num2)
                print(f"Resultado da multiplicação ({num1} * {num2}): {resultado}")
                
            elif opcao == '5':
                texto = input("Digite um texto: ")
                qtd = conn.root.contar_caracteres(texto)
                print(f"O texto tem {qtd} caracteres.")
                
            elif opcao == '6':
                item = input("Digite o item para remover: ")
                sucesso = conn.root.remover_item(item)
                if sucesso:
                    print("Item removido com sucesso!")
                else:
                    print("Erro: Item não encontrado na lista remota.")
                    
            elif opcao == '0':
                print("Encerrando cliente.")
                break
            else:
                print("Opção inválida.")
                
        except EOFError:
            print("Falha na Rede: A conexão com o servidor foi perdida durante a execução.")
            break
        except Exception as e:
            print(f"Ocorreu um erro inesperado na chamada remota: {e}")

if __name__ == "__main__":
    main()