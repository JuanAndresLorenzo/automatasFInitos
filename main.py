# import afnd_to_afd
from minimize_afd import minimize_dfa
from minimize_afd import refine_partition

from afd_class import DFA


print('++++++++++++++++ SELECCIONE UNA OPCION A CONTINUACION ++++++++++++++++')
print("ingrese '1' para transformar un AFND en un AFD")
print("ingrese '2' para transformar un AFND-epsilon en un AFND")
print("ingrese '3' para transformar una Expresion Regular en un AFND-epsilon")
print("ingrese '4' para transformar un AFD en una Expresion Regular")

option = int(input())

if option == 1:
    # afnd_to_afd()
    print('1')

elif option ==2:
    print('1')

elif option==3:
    print('1')

elif option==4:
    estados = input('Ingrese los estados como letras mayusculas, separadas por una coma y sin espacios: ')
    states = []
    for estado in estados:
        if estado!=',':
            states.append(int(estado)) 
    
    alfabeto = input('Ingrese los caracteres del alfabeto, separados por una coma y sin espacios: ')
    alphabet = []
    for caracter in alfabeto:
        if caracter!=',':
            alphabet.append(caracter) 

    transitions = {
        0: {'0': 1, '1': 2},
        1: {'0': 0, '1': 3},
        2: {'0': 3, '1': 0},
        3: {'0': 4, '1': 4},
        4: {'0': 4, '1': 4}
    }

    start_state = int(input('Ingrese el estado inicial: '))

    estados_finales = input('Ingrese los estados finales separados por una coma y sin espacios: ')
    final_states = []
    for estado_final in estados_finales:
        if estado_final!=',':
            final_states.append(int(estado_final))

    afd = DFA(states, alphabet, transitions, start_state, final_states)

    # Llama al método minimize para obtener el AFD minimizado
    afd_minimized = minimize_dfa(afd)

    afd_minimized.print_formated_afd()
else:
    print('El codigo ingresado no es valido')