import tracemalloc
class board:
    #!initializam clasa tablei de sah memorand pozitia, culoarea si tipul piesei
    def __init__(self, col, row, color,type):
        self.col = col
        self.row = row
        self.color = color
        self.type = type
        if self.color != "white" and self.color != "black" or self.type != "pion" and self.type != "tura" and self.type != "nebun" and self.type != "cal" and self.type != "regina" and self.type != "rege" or self.col not in "abcdefgh" or self.row not in range(1, 9):
            raise ValueError("Pozitie/culoare/tip invalid")
    #!functie care returneaza culoarea patratului de pe tabla pe baza paritatii numarului randului, 
    #!si al codului ASCII al coloanei
    @staticmethod
    def gridcolor(col, row):
        if row%2 == 0 and ord(col)%2 != 0:
            return "white"
        elif row%2 == 0:
            return "black"
        if row%2 != 0 and ord(col)%2 == 0:
            return "white"
        elif row%2 != 0:
            return "black"
    '''def verify(col, row):
        if board.row is not None and board.col is not None:
            return True
        else:
            return False
    '''
    #!functie statica care verifica daca pe un patrat se afla o piesa, si returneaza culoarea acesteia, none daca nu exista
    @staticmethod
    def verifica(col, row):
        for piesa in piese:
            if piesa.col == col and piesa.row == row:
                return piesa.color
        return False
    #!functie care returneaza mutarile posibile pentru piesele de tip pion
    def mutari_pion(self):
        lista = []
        #!daca pionul este alb, verifica daca se afla pe randul 2, si daca nu exista o piesa in fata lui, adauga mutarea cu 2 patrate in fata
        if self.color == "white":
            if self.row == 2 and board.verifica(self.col, self.row+2) == False and board.verifica(self.col, self.row+1) == False:
                lista.append(self.col + str((self.row + 2)))
            if board.verifica(self.col, self.row+1) == False:
                lista.append(self.col + str(self.row+1))
            #!verifica daca exista o piesa de culoare neagra pe diagonala stanga sau dreapta, si adauga mutarea in lista
            if board.verifica(chr(int(ord(self.col))+1), self.row+1) == "black":
                lista.append(chr(int(ord(self.col))+1) + str(self.row+1))
            if board.verifica(chr(int(ord(self.col))-1), self.row+1) == "black":
                lista.append(chr(int(ord(self.col))-1) + str(self.row+1))
            #!la fel si pentru negru
        elif self.color == "black":
            if self.row == 7 and board.verifica(self.col, self.row-2) == False:
                lista.append(self.col + str((self.row - 2)))
            if board.verifica(self.col, self.row-1) == False:
                lista.append(self.col + str(self.row-1))
            if board.verifica(chr(int(ord(self.col))+1), self.row-1) == "white":
                lista.append(chr(int(ord(self.col))+1) + str(self.row-1))
            if board.verifica(chr(int(ord(self.col))-1), self.row-1) == "white":
                lista.append(chr(int(ord(self.col))-1) + str(self.row-1))
        return lista

    def mutari_tura(self):
        lista = []
        directii = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #!setam o lista de directii pe care o piesa specifica le poate urma
        for directie in directii:
            dx, dy = directie
            x, y = ord(self.col), self.row
            
            while True:
                x += dx
                y += dy
                #!ne asiguram ca piesa nu iese de pe masa de joc
                if not (ord('a') <= x <= ord('h') and 1 <= y <= 8):
                    break
                #!daca nu exista o piesa pe patratul respectiv, sau daca exista una de culoare diferita, adaugam mutarea in lista
                if board.verifica(chr(x), y) == False or board.verifica(chr(x), y) != self.color:
                    lista.append(chr(x) + str(y))
                    if board.verifica(chr(x), y):
                        break
                else:
                    break

        return lista

    def mutari_nebun(self):
        lista = []
        directii = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for directie in directii:
            dx, dy = directie
            x, y = ord(self.col), self.row
            
            while True:
                x += dx
                y += dy
                
                if not (ord('a') <= x <= ord('h') and 1 <= y <= 8):
                    break
                if board.verifica(chr(x), y) == False or board.verifica(chr(x), y) != self.color:
                    lista.append(chr(x) + str(y))
                    if board.verifica(chr(x), y):
                        break
                else:
                    break

        return lista
    def mutari_cal(self):
        lista = []
        directii = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for directie in directii:
            dx, dy = directie
            x, y = ord(self.col), self.row
            
            if ord('a') <= x + dx <= ord('h') and 1 <= y + dy <= 8:
                if board.verifica(chr(x + dx), y + dy) == False or board.verifica(chr(x + dx), y + dy) != self.color:
                    lista.append(chr(x + dx) + str(y + dy))

        return lista
    def mutari_regina(self):
        lista = []
        lista.extend(self.mutari_tura())
        lista.extend(self.mutari_nebun())
        return lista
    def mutari_rege(self):
        lista = []
        directii = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for directie in directii:
            dx, dy = directie
            x, y = ord(self.col), self.row
            
            if ord(int(self.row)-1) <= x + dx <= ord(int(self.row)+1) and self.row-1 <= y + dy <= self.row+1:
                if board.verifica(chr(x + dx), y + dy) == False or board.verifica(chr(x + dx), y + dy) != self.color:
                    lista.append(chr(x + dx) + str(y + dy))

        return lista
    def mutari(self):
        if self.type == "pion":
            return self.mutari_pion()
        elif self.type == "tura":
            return self.mutari_tura()
        elif self.type == "nebun":
            return self.mutari_nebun()
        elif self.type == "cal":
            return self.mutari_cal()
        elif self.type == "regina":
            return self.mutari_regina()
        elif self.type == "rege":
            return self.mutari_rege()        
    
"""def interfata():
    while True:
        print("Ce vrei sa faci?")
        print("0. Iesi din program")
        print("1. Verifica culoarea unei anumite pozitii")
        print("2. Adauga piesa")
        print("4. Vezi mutari posibile")
        if input() == "0":
            break
        elif input() == "1":
            print("Introdu pozitia")
            col = input()
            row = int(input())
            print(board.verifica(col, row))
        elif input() == "2":
            print("Introduceti pozitia piesei:")
            col = input("Coloana: ")
            row = int(input("Rand: "))
            print("Introduceti culoarea piesei:")
            color = input("Culoare: ")
            print("Introduceti tipul piesei:")
            type = input("Tip: ")
            piesa = board(col, row, color, type)
"""

    
tracemalloc.start()

tura_neagra = board("a", 5, "black", "tura")
tura_neagra = board("a", 5, "black", "tura")
piese = [tura_neagra]
print(tura_neagra.mutari())
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
