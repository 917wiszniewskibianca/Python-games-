
class Menu:
    def __init__(self,game):
        self.game=game

    def start(self):
        self.game.start_game()
        self.handle_menu_option()
    def handle_menu_option(self):
        print(self.game.get_public_view())
        while True:
          try:
            command=input("promt> ")
            if command == "cheat":
                print(self.game)
            else:
                print(self.game.get_public_view())
                words=command.split()
                if words[0] == "warp":
                    x_coord = 0
                    word=words[1]
                    letter=word[0]
                    y_coord=word[1]
                    if y_coord.isdigit() is False:
                        raise IndexError("ERROR: The coordinates should be letter and an integer!")
                    values_for_first_col = ["A", "B", "C", "D", "E", "F", "G", "H"]
                    for i in range(0,8):
                        if values_for_first_col[i]==letter:
                            x_coord= int(i)+1
                            break
                    if x_coord == 0:
                        raise IndexError("ERROR: The coordinate should be on the table!")
                    self.game.move_ship(x_coord,y_coord)
                    print(self.game.get_public_view())
                elif words[0]=="fire":
                    x_coord = 0
                    word = words[1]
                    letter = word[0]
                    y_coord = word[1]
                    if y_coord.isdigit() is False:
                        raise IndexError("ERROR: The coordinates should be letter and an integer!")
                    values_for_first_col = ["A", "B", "C", "D", "E", "F", "G", "H"]
                    for i in range(0, 8):
                        if values_for_first_col[i] == letter:
                            x_coord = int(i) + 1
                            break
                    if x_coord == 0:
                        raise IndexError("ERROR: The coordinate should be on the table!")
                    self.game.fire(x_coord,y_coord)
                    print(self.game.get_public_view())
                    if int(self.game.enemy_ships) == 0:
                        print("YOU WON!!")
                        exit()
                else:
                    raise IndexError("ERROR: The command does not exist!")
          except IndexError as ve:
             print(str(ve))

