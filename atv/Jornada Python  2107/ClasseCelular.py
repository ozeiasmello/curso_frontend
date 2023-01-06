# Classe Celular

# Atributos:
#     Fabricante: String
#     Modelo: String
#     Tela: Decimal
#     Armazenamento: Inteiro
#     Memória: Inteiro
#     Câmera: Inteiro
#     Bateria: Inteiro
#     Tela Ligada: Booleano

# Métodos:
#     ligar_tela()
#     salvar_em_disco()
#     carregar_aplicativo()
#     tirar_foto()
#     verificar_carga_bateria()

class Celular:
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.fcamera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada

    def ligar_tela(self):
        pass

Celular_android = Celular("Samsung", "S10", 6.25, 125, 4, 21, 3400, False) 
