# automatasFInitos
Scripts de python para hacer conversiones entre Automatas FInitos Deterministas, No deterministas, No deterministas Epsilon y Expreciones Regulares.

AFND --> AFD 
    ejemplo:
    ti = transiciones

    delta || t1                | t2 | ... | tn
    ===========================================
    q0    || {q0,q1, ... , qj} | {qp} |   |{ql}
    q1    || {qi}              | {qr} |   |
    .     ||  .                |      |...|
    .     ||  .                |      |   |
    .     ||  .                |      |   |
    qm    || {q0,q1, ... , qj} | {qt} |   | {qk}

    El input que se debe ingresar debe ser de la siguiente forma:
    [[{0,1}, {0}], [{2}, {2}], [{3}, {}], [{3}, {3}]]

    se puede visualizar de mejor forma:
        [
            [{0,1}, {0}],
            [{2}  , {2}],
            [{3}  , {} ], 
            [{3}  , {3}]
        ]