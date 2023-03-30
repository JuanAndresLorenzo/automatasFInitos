#Obtener el AFD
AFD = [[{0,1}, {0}], [{2}, {2}], [{3}, {}], [{3}, {3}]]
final_states = [0, 1, 2]

F = set(final_states)
F_C =  set(range(0,len(AFD))) - F
pi0 = []
pi0.append(F)
pi0.append(F_C)