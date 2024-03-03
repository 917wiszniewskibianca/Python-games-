from random import randint


class Game:
    def __init__(self):
        self.enemy_ships=3
        self.grid = [[" _"] * 10 for i in range(0,10)]


    def __str__(self):
        values_for_first_col = ["A", "B", "C", "D", "E", "F", "G", "H"]
        str_val = "0 1 2 3 4 5 6 7 8  \n"
        for i in range(8):
            if int(i) != 8:
                str_val += values_for_first_col[i]
            for j in range(8):
                str_val += self.grid[i][j]
            if i != 7:
                str_val += "\n"

        return str_val

    def start_game(self):
        self.set_the_stars()
        self.set_the_ship()
        self.place_blingnom_cruises()

    def fire(self,x_coord,y_coord):
        x_coord=int(x_coord)-1
        y_coord=int(y_coord)-1
        if self.can_afis(x_coord,y_coord):
            if self.grid[x_coord][y_coord]==" B":
                print("You destroyed an enemy ship!")
                self.grid[x_coord][y_coord]=" _"
                self.enemy_ships -=1
                self.move_remaining_enemy_ships()
            else:
                raise IndexError("You are not targeting an enemy ship!")
        else:
            raise IndexError("Wrong coordinates!")

    def move_ship(self,x_coord,y_coord):
        x_coord=int(x_coord)
        y_coord=int(y_coord)
        if self.grid[x_coord-1][y_coord-1] == " *":
            raise IndexError("You cannot move on a star!")
        elif self.grid[x_coord-1][y_coord-1]==" B":
            for i in range(1, 9):
                for j in range(1, 9):
                    if self.grid[i][j] == " E":
                        self.grid[i][j] = " _"
            self.grid[x_coord-1][y_coord -1] = " E"

            print("GAME OVER!!")
            exit()
        else:
            for i in range(0,8):
                for j in range(0,8):
                    if self.grid[i][j]==" E":
                        self.grid[i][j]=" _"
            self.grid[x_coord-1][y_coord-1]=" E"

    def move_remaining_enemy_ships(self):
        for i in range(1,8):
           for j in range(1,8):
              if self.grid[i][j]== " B":
                ship_relocated=False
                while ship_relocated!= True:
                  x_coord=randint(1,8)
                  y_coord=randint(1,8)
                  if self.grid[x_coord][y_coord]==" _":
                      self.grid[x_coord][y_coord]= " B"
                      self.grid[i][j]=" _"
                      ship_relocated=True



    def get_public_view(self):
        values_for_first_col = ["A", "B", "C", "D", "E", "F", "G", "H"]
        str_val = "0 1 2 3 4 5 6 7 8  \n"
        for i in range(8):
            if int(i) != 8:
                str_val += values_for_first_col[i]
            for j in range(8):
                if self.grid[i][j]!=' B':
                  str_val += self.grid[i][j]
                elif self.can_afis(i,j):
                    str_val+=self.grid[i][j]
                else:
                    str_val+=" _"
            if i != 7:
                str_val += "\n"

        return str_val

    def can_afis(self,x_coord,y_coord):
        x_coord= int(x_coord)
        y_coord=int(y_coord)
        if self.grid[x_coord-1][y_coord] ==" E" or self.grid[x_coord-1][y_coord-1]==" E" or self.grid[x_coord-1][y_coord+1]==" E" or \
             self.grid[x_coord][y_coord-1]==" E" or self.grid[x_coord][y_coord+1]==" E" or self.grid[x_coord+1][y_coord]==" E" or self.grid[x_coord+1][y_coord-1]== " E" \
             or self.grid[x_coord+1][y_coord]==' E' or self.grid[x_coord+1][y_coord+1]==' E':
                return True
        else :
            return False

    def set_the_stars(self):
        stars_set = 0
        while stars_set < 10:
            x_coord = randint(1, 8)
            y_coord = randint(1, 8)
            if self.validate_place_and_set_elements(x_coord, y_coord, "staar") == True:
                stars_set= stars_set + 1

    def set_the_ship(self):
        ship_placed = False
        while ship_placed == False:
            x_coord = randint(1, 8)
            y_coord = randint(1, 8)
            if self.validate_place_and_set_elements(x_coord, y_coord, "ship"):
                ship_placed = True

    def place_blingnom_cruises(self):
        blingnom_sets = 0
        while blingnom_sets < 3:
            x_coord = randint(1, 8)
            y_coord = randint(1, 8)
            if self.grid[x_coord-1][y_coord-1] == " _":
                self.grid[x_coord-1][y_coord-1] = " B"
                blingnom_sets = blingnom_sets+1

    def validate_place_and_set_elements(self, x_coord, y_coord, argument):
        x_coord = int(x_coord)
        y_coord = int(y_coord)
        if self.grid[x_coord-1][y_coord-1] == " _":
          if (self.grid[x_coord][y_coord - 1] == " _" or self.grid[x_coord][y_coord - 1] in ["A","B","C","D","E","F","G","H"] or self.grid[x_coord-1][y_coord] in ["0","1","2","3","4","5","6","7","8"]) and self.grid[x_coord][ y_coord + 1] == " _":
            if  self.grid[x_coord + 1][y_coord] == " _" and (self.grid[x_coord - 1][y_coord] == " _" or self.grid[x_coord-1][y_coord] in ["0","1","2","3","4","5","6","7","8"]):
              if (self.grid[x_coord - 1][y_coord - 1] == " _" or self.grid[x_coord][y_coord - 1] in ["A","B","C","D","E","F","G","H"] or  self.grid[x_coord-1][y_coord] in ["0","1","2","3","4","5","6","7","8"]) and self.grid[x_coord - 1][y_coord + 1] == " _":
                if (self.grid[x_coord + 1][y_coord - 1] == " _" or self.grid[x_coord][y_coord - 1] in ["A","B","C","D","E","F","G","H"] or self.grid[x_coord-1][y_coord] in ["0","1","2","3","4","5","6","7","8"] ) and self.grid[x_coord + 1][y_coord + 1] == " _":
                   if argument =="staar":
                        self.grid[x_coord-1][y_coord-1] = " *"
                        return True
                   elif argument == "ship":
                        self.grid[x_coord-1][y_coord-1] = " E"
                        return True