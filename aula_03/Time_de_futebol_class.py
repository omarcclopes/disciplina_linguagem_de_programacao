# criando classe Time_de_Futebol()
class Time_de_Futebol():

    def __init__(self, nome, idade, estado, gols):
        self.nome = nome
        self.idade = idade
        self.estado = estado
        self.gols = gols

    def jogar(self):
        print(self.nome.title() + " está jogando.")

    def marcar_gol(self):
        self.gols = self.gols + 1
        print(self.nome.title() + " fez um gol.")
       
    def ver_placar(self):
        print(self.nome.title() + ' está com ' + str(self.gols) + ' gols.')

    def ver_idade(self):
        print(self.nome.title() + ' está com ' + str(self.idade) + ' anos de fundação.')
     