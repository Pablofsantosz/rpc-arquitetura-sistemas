import rpyc
import time

class CalculadoraService(rpyc.Service):
   
    lista_compartilhada = [] 

    
    def exposed_somar(self, a, b): 
        return a + b

    def exposed_adicionar_item(self, item):
        self.__class__.lista_compartilhada.append(item) 
        return self.__class__.lista_compartilhada

    def exposed_demorar(self, segundos):
        time.sleep(int(segundos)) 
        return "ok" 

    
    def exposed_contar_caracteres(self, texto):
        """Manipula texto: retorna a quantidade de caracteres."""
        return len(str(texto))

    def exposed_multiplicar(self, a, b):
        """Manipula números: retorna a multiplicação de dois valores."""
        return a * b
        
    def exposed_remover_item(self, item):
        """Manipula lista: remove um item específico da lista compartilhada."""
        try:
            self.__class__.lista_compartilhada.remove(item)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(CalculadoraService, port=18861)
    print("Servidor RPC iniciado na porta 18861...")
    server.start()