# criando times
from Time_de_futebol_class import Time_de_Futebol

time_a = Time_de_Futebol('Palmeiras', 106,'São Paulo', 0)
time_b = Time_de_Futebol('Santos', 108,'São Paulo', 0)

time_a.ver_idade()
time_b.ver_idade()

time_a.jogar()
time_a.marcar_gol()
time_a.ver_placar()

time_b.jogar()
time_b.marcar_gol()
time_b.marcar_gol()
time_b.marcar_gol()

time_a.marcar_gol()

time_b.ver_placar()
time_a.ver_placar()