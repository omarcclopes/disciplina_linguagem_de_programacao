# criando classe aviao
class Aviao():

    def __init__(self, modelo, capacidade, comprimento):
        self.modelo = modelo
        self.capacidade = capacidade
        self.comprimento = comprimento

    def decolar(self):
        print(self.modelo.title() + " agora está decolando.")

    def aterrisar(self):
        print(self.modelo.title() + " aterrisou no destino.")

    def taxiar(self):
        print(self.modelo.title() + " está taxiando na pista.")  

    def remover_passageiro(self):
        self.capacidade = self.capacidade - 1   
        print(self.modelo.title() + " teve um passageiro removido.")  

    def verificar_lotacao(self):
        print(self.modelo.title() + " está com " + str(self.capacidade) + ' passageiros à bordo.')