# criando aviões
from aviao_class import Aviao

aviao_a = Aviao('Airbus A380', 615, 72)
aviao_b = Aviao('Boeing 747', 410, 76)

aviao_a.verificar_lotacao()
aviao_a.remover_passageiro()
aviao_a.verificar_lotacao()
aviao_a.taxiar()
aviao_a.decolar()

aviao_b.taxiar()
aviao_b.decolar()
aviao_b.aterrisar()
aviao_b.verificar_lotacao()
aviao_b.remover_passageiro()
aviao_b.verificar_lotacao()