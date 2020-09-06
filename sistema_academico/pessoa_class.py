class Pessoa():

    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def verificar_genero(self):
        print('{} é do gênero {} e tem {} anos.'.format(self.nome, self.genero, self.idade))

class Aluno(Pessoa):

    def __init__(self, nome, idade, genero, periodo, curso):
        super().__init__(nome, idade, genero)
        self.periodo = periodo
        self.curso = curso

    def ver_curso_periodo(self):
        print('{} está cursando {} no {} período' .format(self.nome, self.curso, self.periodo)) 

class Responsavel(Pessoa):

    def __init__(self, nome, idade, genero, cpf, dependente, curso):
        super().__init__(nome, idade, genero)
        self.cpf = cpf
        self.dependente = dependente
        self.curso = curso

    def matricular_filhos(self):
        print("{}, portando o CPF {}, matriculou {}, para cursar {} neste período letivo.".format(self.nome, self.cpf, self.dependente, self.curso))  
        
class Professor(Pessoa):

    def __init__(self, nome, idade, genero, disciplina, curso, periodo):
        super().__init__(nome, idade, genero)
        self.disciplina = disciplina
        self.curso = curso
        self.periodo = periodo

    def aplicar_prova(self):
        print('{}, está aplicando a avaliação de {}, no {} período de {}.' .format(self.nome, self.disciplina, self.periodo, self.curso))

class Coordenador(Pessoa):

    def __init__(self, nome, idade, genero, curso):
        super().__init__(nome, idade, genero)
        self.curso = curso 

    def reuniao_docente(self):
        print('{} que coordena o curso de {}, está realizando uma reunião com os docentes.'.format(self.nome, self.curso))

class Diretor(Pessoa):

    def __init__(self, nome, idade, genero, instituicao):
        super().__init__(nome, idade, genero)
        self.instituicao = instituicao

    def reuniao_geral(self):
        print('{}, que dirige a {}, convocou uma reunião geral.'.format(self.nome, self.instituicao))
