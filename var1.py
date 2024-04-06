import tracemalloc
pion_alb = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0]]

pion_negru = [[0,0,0,0,0,0,0,0],
              [0,1,1,1,1,1,1,1],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]]

nebun_alb = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,1,0,0,1,0,0]]

nebun_negru = [[0,0,1,0,0,1,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]

tura_alb = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,1]]

tura_negru = [[1,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]]

cal_alb = [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,1,0,0,0,0,1,0]]

cal_negru = [[0,1,0,0,0,0,1,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]

regina_alb = [[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0]]

regina_negru = [[0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]

rege_alb = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0]]

rege_negru = [[0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]]
coloane = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
def afisare(printare = 0):
    masa = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]
    piese = {
        "pion_alb": "♙",
        "pion_negru": "♟",
        "nebun_alb": "♗",
        "nebun_negru": "♝",
        "tura_alb": "♖",
        "tura_negru": "♜",
        "cal_alb": "♘",
        "cal_negru": "♞",
        "regina_alb": "♕",
        "regina_negru": "♛",
        "rege_alb": "♔",
        "rege_negru": "♚"
    }
    for randuri in range(8):
        for coloane in range(8):
            for piesa, simbol in piese.items():
                if globals()[piesa][randuri][coloane] == 1:
                    masa[randuri][coloane] = simbol
    if printare == 1:
        print("  a b c d e f g h")
        print("  ----------------")
        for randuri in range(8):
            print(randuri, end="|")
            for coloane in range(8):
                print(masa[randuri][coloane], end = ' ')
            print("|")
        print("  ----------------")
        
    return masa

def afisare_posibilitati(lista_posibilitati):
    masa = afisare()
    piese = {
        "pion_alb": "♙",
        "pion_negru": "♟",
        "nebun_alb": "♗",
        "nebun_negru": "♝",
        "tura_alb": "♖",
        "tura_negru": "♜",
        "cal_alb": "♘",
        "cal_negru": "♞",
        "regina_alb": "♕",
        "regina_negru": "♛",
        "rege_alb": "♔",
        "rege_negru": "♚"
    }
    if len(lista_posibilitati) == 0:
        print("eroare")
    for mutare in lista_posibilitati:
        rand_mutare, coloana_mutare = mutare
        buffer = masa[rand_mutare][coloana_mutare]
        masa[rand_mutare][coloana_mutare] = "*"
        print(chr(int(coloana_mutare) + 97), rand_mutare)
        print("  a b c d e f g h")
        print("  ----------------")
        for randuri in range(8):
            print(randuri, end="|")
            for coloane in range(8):
                print(masa[randuri][coloane], end = ' ')
            print("|")
        print("  ----------------")
        masa[rand_mutare][coloana_mutare] = buffer
        print()
        print()
        



def concatenare_piesealbe():
    piese_albe = [[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
    for i in range(8):
        for j in range(8):
            if pion_alb[i][j] == 1:
                piese_albe[i][j] = 1
            if nebun_alb[i][j] == 1:
                piese_albe[i][j] = 1
            if tura_alb[i][j] == 1:
                piese_albe[i][j] = 1
            if cal_alb[i][j] == 1:
                piese_albe[i][j] = 1
            if regina_alb[i][j] == 1:
                piese_albe[i][j] = 1
            if rege_alb[i][j] == 1:
                piese_albe[i][j] = 1
    return piese_albe

def concatenare_piesenegre():
    piese_negre = [[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
    for i in range(8):
        for j in range(8):
            if pion_negru[i][j] == 1:
                piese_negre[i][j] = 1
            if nebun_negru[i][j] == 1:
                piese_negre[i][j] = 1
            if tura_negru[i][j] == 1:
                piese_negre[i][j] = 1
            if cal_negru[i][j] == 1:
                piese_negre[i][j] = 1
            if regina_negru[i][j] == 1:
                piese_negre[i][j] = 1
            if rege_negru[i][j] == 1:
                piese_negre[i][j] = 1
    
    return piese_negre


def mutare_pion(coloana_piesa, rand_piesa):
    mutari_posibile = []
    if pion_alb[rand_piesa][coloane[coloana_piesa]] == 1:
        if rand_piesa == 6 and concatenare_piesealbe()[rand_piesa - 2][coloane[coloana_piesa]] == 0:
            mutari_posibile.append((rand_piesa - 2, coloane[coloana_piesa]))
        if concatenare_piesealbe()[rand_piesa - 1][coloane[coloana_piesa]] == 0 and concatenare_piesenegre()[rand_piesa - 1][coloane[coloana_piesa]] == 0:
            mutari_posibile.append((rand_piesa - 1, coloane[coloana_piesa]))
        if concatenare_piesenegre()[rand_piesa - 1][coloane[coloana_piesa] + 1] == 1:
            mutari_posibile.append((rand_piesa - 1, coloane[coloana_piesa] + 1))
        if concatenare_piesenegre()[rand_piesa - 1][coloane[coloana_piesa] - 1] == 1:
            mutari_posibile.append((rand_piesa - 1, coloane[coloana_piesa] - 1))
    if pion_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        if rand_piesa == 1 and concatenare_piesenegre()[rand_piesa + 2][coloane[coloana_piesa]] == 0:
            mutari_posibile.append((rand_piesa + 2, coloane[coloana_piesa]))
        if concatenare_piesenegre()[rand_piesa + 1][coloane[coloana_piesa]] == 0 and concatenare_piesealbe()[rand_piesa + 1][coloane[coloana_piesa]] == 0:
            mutari_posibile.append((rand_piesa + 1, coloane[coloana_piesa]))
        if concatenare_piesealbe()[rand_piesa + 1][coloane[coloana_piesa] + 1] == 1:
            mutari_posibile.append((rand_piesa + 1, coloane[coloana_piesa] + 1))
        if concatenare_piesealbe()[rand_piesa + 1][coloane[coloana_piesa] - 1] == 1:
            mutari_posibile.append((rand_piesa + 1, coloane[coloana_piesa] - 1))
    print(mutari_posibile)
    return mutari_posibile

def mutare_tura(coloana_piesa, rand_piesa):
    directii = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    mutari_posibile = []

    for directie in directii:
        dx, dy = directie
        x, y = rand_piesa, coloane[coloana_piesa]
        while True:
            x += dx
            y += dy
            if not (0 <= x <= 7 and 0 <= y <= 7):
                break
            if concatenare_piesealbe()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesealbe()[x][y] == 0:
                    if concatenare_piesenegre()[x][y] == 1:
                        mutari_posibile.append((x, y))
                        break
                    mutari_posibile.append((x, y))
                else:
                    break
            if concatenare_piesenegre()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesenegre()[x][y] == 0:
                    if concatenare_piesealbe()[x][y] == 1:
                        mutari_posibile.append((x, y))
                        break
                    mutari_posibile.append((x, y))
                else:
                    break    
    return mutari_posibile

def mutare_nebun(coloana_piesa, rand_piesa):
    directii = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    mutari_posibile = []

    for directie in directii:
        dx, dy = directie
        x, y = rand_piesa, coloane[coloana_piesa]
        while True:
            x += dx
            y += dy
            if not (0 <= x <= 7 and 0 <= y <= 7):
                break
            if concatenare_piesealbe()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesealbe()[x][y] == 0:
                    if concatenare_piesenegre()[x][y] == 1:
                        mutari_posibile.append((x, y))
                        break
                    mutari_posibile.append((x, y))
                else:
                    break
            if concatenare_piesenegre()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesenegre()[x][y] == 0:
                    if concatenare_piesealbe()[x][y] == 1:
                        mutari_posibile.append((x, y))
                        break
                    mutari_posibile.append((x, y))
                else:
                    break    
    return mutari_posibile

def mutare_cal(coloana_piesa, rand_piesa):
    mutari_posibile = []

    directii = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for directie in directii:
        dx, dy = directie
        x, y = rand_piesa, coloane[coloana_piesa]
        x += dx
        y += dy
        if 0 <= x <= 7 and 0 <= y <= 7:
            if concatenare_piesealbe()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesealbe()[x][y] == 0:
                    mutari_posibile.append((x, y))

            if concatenare_piesenegre()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesenegre()[x][y] == 0:
                    mutari_posibile.append((x, y))
    return mutari_posibile

def mutare_regina(coloana_piesa, rand_piesa):
    mutari_posibile = []

    mutari_posibile.extend(mutare_tura(coloana_piesa, rand_piesa))
    mutari_posibile.extend(mutare_nebun(coloana_piesa, rand_piesa))
    return mutari_posibile

def mutare_rege(coloana_piesa, rand_piesa):
    mutari_posibile = []

    directii = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for directie in directii:
        dx, dy = directie
        x, y = rand_piesa, coloane[coloana_piesa]
        x += dx
        y += dy
        if 0 <= x <= 7 and 0 <= y <= 7:
            if concatenare_piesealbe()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesealbe()[x][y] == 0:
                    if concatenare_piesenegre()[x][y] == 1:
                        mutari_posibile.append((x, y))
                else:
                    if concatenare_piesenegre()[x][y] == 1:
                        mutari_posibile.append((x, y))
            if concatenare_piesenegre()[rand_piesa][coloane[coloana_piesa]] == 1:
                if concatenare_piesenegre()[x][y] == 0:
                    if concatenare_piesealbe()[x][y] == 1:
                        mutari_posibile.append((x, y))
                else:
                    if concatenare_piesealbe()[x][y] == 1:
                        mutari_posibile.append((x, y))
    return mutari_posibile

def posibilitati(coloana_piesa, rand_piesa, lista = 0):
    mutari_posibile = []
    if pion_alb[rand_piesa][coloane[coloana_piesa]] == 1 or pion_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        mutari_posibile = mutare_pion(coloana_piesa, rand_piesa)
    if tura_alb[rand_piesa][coloane[coloana_piesa]] == 1 or tura_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        mutari_posibile = mutare_tura(coloana_piesa, rand_piesa)
    if nebun_alb[rand_piesa][coloane[coloana_piesa]] == 1 or nebun_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        mutari_posibile = mutare_nebun(coloana_piesa, rand_piesa)
    if cal_alb[rand_piesa][coloane[coloana_piesa]] == 1 or cal_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        mutari_posibile = mutare_cal(coloana_piesa, rand_piesa)
    if regina_alb[rand_piesa][coloane[coloana_piesa]] == 1 or regina_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        mutari_posibile = mutare_regina(coloana_piesa, rand_piesa)
    if rege_alb[rand_piesa][coloane[coloana_piesa]] == 1 or rege_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        mutari_posibile = mutare_rege(coloana_piesa, rand_piesa)
    if lista == 0:
        return afisare_posibilitati(mutari_posibile)
    else:
        return mutari_posibile
def mutare(coloana_piesa, rand_piesa, coloana_mutare, rand_mutare):
    if pion_alb[rand_piesa][coloane[coloana_piesa]] == 1:
        pion_alb[rand_piesa][coloane[coloana_piesa]] = 0
        pion_alb[rand_mutare][coloane[coloana_mutare]] = 1
    if pion_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        pion_negru[rand_piesa][coloane[coloana_piesa]] = 0
        pion_negru[rand_mutare][coloane[coloana_mutare]] = 1
    if tura_alb[rand_piesa][coloane[coloana_piesa]] == 1:
        tura_alb[rand_piesa][coloane[coloana_piesa]] = 0
        tura_alb[rand_mutare][coloane[coloana_mutare]] = 1
    if tura_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        tura_negru[rand_piesa][coloane[coloana_piesa]] = 0
        tura_negru[rand_mutare][coloane[coloana_mutare]] = 1
    if nebun_alb[rand_piesa][coloane[coloana_piesa]] == 1:
        nebun_alb[rand_piesa][coloane[coloana_piesa]] = 0
        nebun_alb[rand_mutare][coloane[coloana_mutare]] = 1
    if nebun_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        nebun_negru[rand_piesa][coloane[coloana_piesa]] = 0
        nebun_negru[rand_mutare][coloane[coloana_mutare]] = 1
    if cal_alb[rand_piesa][coloane[coloana_piesa]] == 1:
        cal_alb[rand_piesa][coloane[coloana_piesa]] = 0
        cal_alb[rand_mutare][coloane[coloana_mutare]] = 1
    if cal_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        cal_negru[rand_piesa][coloane[coloana_piesa]] = 0
        cal_negru[rand_mutare][coloane[coloana_mutare]] = 1
    if regina_alb[rand_piesa][coloane[coloana_piesa]] == 1:
        regina_alb[rand_piesa][coloane[coloana_piesa]] = 0
        regina_alb[rand_mutare][coloane[coloana_mutare]] = 1
    if regina_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        regina_negru[rand_piesa][coloane[coloana_piesa]] = 0
        regina_negru[rand_mutare][coloane[coloana_mutare]] = 1
    if rege_alb[rand_piesa][coloane[coloana_piesa]] == 1:
        rege_alb[rand_piesa][coloane[coloana_piesa]] = 0
        rege_alb[rand_mutare][coloane[coloana_mutare]] = 1
    if rege_negru[rand_piesa][coloane[coloana_piesa]] == 1:
        rege_negru[rand_piesa][coloane[coloana_piesa]] = 0
        rege_negru[rand_mutare][coloane[coloana_mutare]] = 1

def joc():
    while True:
        print("ALB MUTA")
        afisare(1)
        coloana = input("Coloana piesei pe care doriti sa o mutati: ")
        rand = int(input("Randul piesei pe care doriti sa o mutati: "))
        if concatenare_piesealbe()[rand][coloane[coloana]] == 0:
            print("Nu exista piesa pe aceasta pozitie")
            return 0
        posibilitati(coloana, rand)
        coloana_mutare = input("Coloana unde doriti sa mutati piesa: ")
        rand_mutare = int(input("Randul unde doriti sa mutati piesa: "))
        if (rand_mutare, coloane[coloana_mutare]) in posibilitati(coloana, rand, 1):
            mutare(coloana, rand, coloana_mutare, rand_mutare)
        else:
            print("Mutare invalida")
        print("NEGRU MUTA")
        afisare(1)
        coloana = input("Coloana piesei pe care doriti sa o mutati: ")
        rand = int(input("Randul piesei pe care doriti sa o mutati: "))
        if concatenare_piesenegre()[rand][coloane[coloana]] == 0:
            print("Nu exista piesa pe aceasta pozitie")
            return 0
        posibilitati(coloana, rand)
        coloana_mutare = input("Coloana unde doriti sa mutati piesa: ")
        rand_mutare = int(input("Randul unde doriti sa mutati piesa: "))
        if (rand_mutare, coloane[coloana_mutare]) in posibilitati(coloana, rand, 1):
            mutare(coloana, rand, coloana_mutare, rand_mutare)
        else:
            print("Mutare invalida")

tracemalloc.start()
print(posibilitati("a", 0, 1))
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
