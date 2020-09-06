print('========================================')
print('PESSOAS:')
from pessoa_class import Pessoa

maria = Pessoa("Maria", 24, "feminino")
joao = Pessoa("João", 35, "masculino")

#verificando o genero da pessoa
maria.verificar_genero()
joao.verificar_genero()

print('========================================')
print('ALUNOS:')
from pessoa_class import Aluno

astolfo = Aluno('Astolfo', 34, 'masculino','2º','GTI')
epaminondas = Aluno('Epaminondas', 54, 'masculino','3º','Direito')

#curso e período
astolfo.ver_curso_periodo()
epaminondas.ver_curso_periodo()

print('========================================')
print('RESPONSÁVEIS:')
from pessoa_class import Responsavel

felizberto = Responsavel('Felizberto', 54, 'masculino', '999.999.999-99', 'Mariana', 'Pedagogia')
diana = Responsavel('Diana', 39, 'feninino', '555.555.555-55', 'Pedro', 'Administração')

#Matriculando os dependentes
diana.matricular_filhos()
felizberto.matricular_filhos()

print('========================================')
print('PROFESSORES:')
from pessoa_class import Professor

alberto = Professor('Alberto',55,'masculino','matemática','Ciências Contábeis','1º' )
monica = Professor('Mônica', 40, 'feninino', 'português', 'Pedagogia', '4º')

#Aplicando provas
alberto.aplicar_prova()
monica.aplicar_prova()

print('========================================')
print('COORDENADORES:')
from pessoa_class import Coordenador

oscar = Coordenador('Oscar',45,'masculino','Administração')
sara = Coordenador('Sara', 38,'feminino','Direito')

#Fazendo uma reunião
oscar.reuniao_docente()
sara.reuniao_docente()

print('========================================')
print('DIRETORES:')
from pessoa_class import Diretor

dumbledore = Diretor('Dumbledore',150,'masculino','Escola Hogwarts')
daenerys = Diretor('Daenerys', 24, 'feminino','Faculdade Dothrak')

#Fazendo uma reunião geral
dumbledore.reuniao_geral()
daenerys.reuniao_geral()

print('========================================')