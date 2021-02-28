import random


def within_boundary(num):
    """
    checks to see if number input is within game board boundary
    """
    if num < 0 or num > 9:
        return False
    else:
        return True




def is_sunk(ship):
    """
    returns Boolean value, which is True 
    if ship is sunk and False otherwise
    """

    ship_length = ship[3]
    amount_hits = ship[4]
    if len(amount_hits) == ship_length:
        return True
    else:
        return False



def ship_type(ship):
    """
    returns one of the strings "battleship", "cruiser", 
    "destroyer", or "submarine" identifying the type of ship
    """ 

    length = ship[3]
    if length == 1:
        return 'submarine'
    elif length == 2:
        return 'destroyer'
    elif length == 3:
        return 'cruiser'
    elif length == 4:
        return 'battleship'
    else:
        return 'Not ship type, please try again'
        


def is_adjacent(sr, sc, row, column):
    """
    New function added as an extension/helper to is_open_sea function. 
    Each sr and sc consists of ship row and column, this ship row and column is compared with the row and column 
    to check if the given coordinates are adjacent at any point. This function is used in a loop during is_open_sea function so check
    if the occupied squares of a ship are adjacent.
    """

    if (sr,sc) == (row+1, column):
        return True
    elif (sr,sc) == (row, column-1):
        return True
    elif (sr,sc) == (row, column+1):
        return True
    elif (sr,sc) == (row-1, column):
        return True
    elif (sr,sc) == (row+1, column-1):
        return True
    elif (sr,sc) == (row-1, column-1):
        return True
    elif (sr,sc) == (row-1, column+1):
        return True
    elif (sr,sc) == (row+1, column+1):
        return True
    else:
       return False





def is_open_sea(row, column, fleet):
    """
    checks if the square given by row and column neither contains nor is adjacent (horizontally, vertically, or diagonally)
    to some ship in fleet. Returns Boolean True if so and False otherwise
    """
    open_count = 0

    for ship in fleet:
        horizontal = ship[2]
        length = ship[3]
        if length == 1:
            if is_adjacent(ship[0], ship[1], row, column):
                return False
            else:
                open_count += 1
        else:
            if horizontal == True:
                for i in range(ship[1], (ship[1]+length)): # Iterating through coordinates within the ship. column is changed if horizontal == False, row otherwise.      
                    if is_adjacent(ship[0], i, row, column): # If any of the occupied coordinates are adjacent with given row and column, return false
                        return False
                else:
                    open_count += 1

            elif horizontal == False:
                for j in range(ship[0], (ship[0]+length)):
                    if is_adjacent(j, ship[1], row, column):
                        return False
                else:
                    open_count += 1

    # confirmation of each ship passes the open sea function, if the count is equal to the len of the fleet (each ship instance), then we can confirm and mark as true.
    if open_count == len(fleet):
        return True


            


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    '''
    checks if addition of a ship, specified by row, column, horizontal, and length as in ship representation above, 
    to the fleet results in a legal arrangement (see the figure above). If so, the function returns Boolean True and it returns False otherwise.
    '''
    
    if not within_boundary(row):
        return "Row input out of bounds!"

    if not within_boundary(column):
        return "Column input out of bounds!"

        
    if is_open_sea(row, column, fleet): 
        # First check to see if ship plotting is horizontal or not
        if horizontal == True:
            if not within_boundary((column+length)-1): # if the length of the ship falls outside the boundary then placing cannot proceed
                return False
            else:
                for i in range(column, (column+length)): # Iterating through coordinates within the ship. column is change if horizontal == False, row otherwise.
                    for ship in fleet:
                        if (ship[0],ship[1]) == (row, i): # If the coordinates are the same 
                            return False
                return True
        elif horizontal == False:
            if not within_boundary((row+length) -1):
                return False
            else:
                for j in range(row, (row+length)):
                    for ship in fleet:
                        if (ship[0],ship[1]) == (j, column):
                            return False
                return True
    else:
        return False




def place_ship_at(row, column, horizontal, length, fleet):
    '''
    returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, and length 
    as in ship representation above, to fleet.
    '''
    ship = (row, column, horizontal, length, set())
    fleet.append(ship)
    return fleet




def randomly_place_all_ships():
    '''
    returns a fleet that is a result of a random legal arrangement of the 10 ships in the ocean.
    '''

    fleet = []
    battleship = 1
    cruisers = 2
    destroyers = 3
    submarines = 4
    

    while battleship > 0:
        row = random.randint(0,9)
        column = random.randint(0,9)
        random_bit = random.getrandbits(1)
        horizontal = bool(random_bit)
        length = 4
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
            battleship -= 1


    while cruisers > 0:
        row = random.randint(1,9)
        column = random.randint(1,9)
        random_bit = random.getrandbits(1)
        horizontal = bool(random_bit)
        length = 3
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
            cruisers -= 1


    while destroyers > 0:
        row = random.randint(1,9)
        column = random.randint(1,9)
        random_bit = random.getrandbits(1)
        horizontal = bool(random_bit)
        length = 2
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
            destroyers -= 1

    while submarines > 0:
        row = random.randint(1,9)
        column = random.randint(1,9)
        random_bit = random.getrandbits(1)
        horizontal = bool(random_bit)
        length = 1
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
            submarines -= 1

    return fleet





def check_if_hits(row, column, fleet):
    '''
    returns Boolean value, which is True if the shot of the human player at the square 
    represented by row and column hits any of the ships of fleet, and False otherwise
    '''

    for ship in fleet:
        horizontal = ship[2]
        length = ship[3]
        if length == 1:
            if (row, column) == (ship[0], ship[1]):
                return True
        else:
            if horizontal == True:
                for i in range(ship[1], (ship[1]+length)): # Iterating through shipdinates within the ship. column is change if horizontal == False, row otherwise.
                    if (row, column) == (ship[0],i): # If the shipdinates are the same 
                        return True

            elif horizontal == False:
                for j in range(ship[0], (ship[0]+length)):
                    if (row, column) == (j, ship[1]):
                        return True
                    
    else:
        return False



def already_hit(row, column, fleet):
    '''
    Function checks to see if the given row and column have already been used to hit are ship position.
    '''

    for ship in fleet:
        hits = ship[4]
        for tup in hits:
            if tup == (row,column):
                return True

    return False



def already_missed(row, column, missed):
    '''
    Function checks to see if given row and column are contained in a missed set. This variable is created in game.
    '''

    for coor in missed:
        if (row, column) == coor:
            return True 
    return False

    


def hit(row, column, fleet):
    '''
    returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that receives a hit by the shot 
    at the square represented by row and column, and fleet1 is the fleet resulting from this hit.
    '''

    for ship in fleet:
        horizontal = ship[2]
        length = ship[3]
        hit = ship[4]
        if length == 1:
            if (row, column) == (ship[0], ship[1]):
                hit.add((row,column))
                return fleet, ship
        else:
            if horizontal == True:
                for i in range(ship[1], (ship[1]+length)): # Iterating through coordinates within the ship. column is change if horizontal == False, row otherwise.
                    if (row, column) == (ship[0],i): # If the coordinates are the same 
                        hit.add((row,column))
                        return fleet, ship
            elif horizontal == False:
                for j in range(ship[0], (ship[0]+length)):
                    if (row, column) == (j, ship[1]):
                        hit.add((row,column))
                        return fleet, ship





def are_unsunk_ships_left(fleet):
    '''
    returns Boolean value, which is True if there are ships in the fleet that are still not sunk, and False otherwise
    '''

    sunk_count = 0
    for ship in fleet:
        if is_sunk(ship):
            sunk_count += 1

    if sunk_count == len(fleet):
        return False
    else:
        return True






def main():
    print("LETS PLAY BATTLESHIPS!!")

    fleet = []
    choosing = True

    # Input check to see if the user wants to continue playing. If the user selects yes, ships are generated. If no, the game exits any other input is not accepted.
    while choosing == True:
        choice = input("Do you want to start a game? yes or no (type exit to leave):  ")
        if choice.strip().lower() == "exit":
            exit()
        elif choice.strip().lower() == "yes":
            fleet = randomly_place_all_ships()
            choosing = False

        elif choice.strip().lower() == "no":
            exit()
        else:
            print("Please enter one of the following inputs! yes, no: ")
    

    # Initialising the game, and creating the board.
    game_over = False
    shots = 0
    missed = set()
    board = []



    class Cell:
        """
        :param x: x-axis location
        :param y: y-axis location
        """
        def __init__(self, row, col):
            self.row = int(row)
            self.col = int(col)
            self.visual = ". "

        def __str__(self):
            return self.visual

    class Board:

        def __init__(self, row=10, col=10, show_labels=False):
            """
            :param x: How many columns the board uses
            :param y: How many rows the board uses
            :param show_labels: Display labels to the player
            """

            self.row = row + 1
            self.col = col + 1
            self.show_labels = show_labels
            self.board = {}

            self.generate_board()

        def generate_board(self):
            for y in range(0, self.col):

                # Add the key X to the board dictionary
                self.board[y] = []   

                for x in range(0, self.row):
                    # Make a cell @ the current x, y and add it to the board
                    cell = Cell(x, y)
                    self.board[y].append(cell)

        def show_board(self):

            for key, cells in self.board.items():

                # Add the X Labels
                if self.show_labels:
                    if key == 0:
                        row_label = []
                        for cell in self.board[key]:
                            row_label.append(str(cell.row))
                        print(" ".join(row_label))

                rows = []
                for cell in cells:
                    rows.append(str(cell))

                # Add the Y labels
                if self.show_labels:
                    rows.append(str(cell.col))

                print("".join(rows))

        def set_hit(self, row, col, plot = "* "):
            self.board[row][col].visual = plot

        def set_miss(self, row, col):
            self.board[row][col].visual = "/ "


    b = Board(9, 9, True)
    b.show_board()

    while not game_over:

        '''
        While loop and exception handling for possible inputs, if the coordinates are not spaced or too high, input is not accepted
        '''

        inputting = True
        while inputting == True:
            try:
                loc_str = input("Enter row and column to shoot (separted by space) - or type exit to leave: ")
                loc_str = loc_str.strip() # remove leading or trailing whitespace
                if loc_str.lower() == "exit": # Allow user to exit game whenever they please
                    exit()
                loc_str = loc_str.split()
            
                if (not within_boundary(int(loc_str[0])) & within_boundary(int(loc_str[1]))): # If input value is too large, small error handling is placed.
                    print("Invalid coordinates placed, please enter coordinates between 0 and 9: ")
                    print("\n")
                else:
                    inputting = False

            except IndexError: # For non spaced inputs, this error is raised as input cannot be split.
                print("Input not spaced, please try again: ")
                print("\n")

            except ValueError: # For any other characters other than numbers are added, this exception is triggered
                print("Invalid characters added, please place correct inputs!")
                print("\n")




        # Once inouts are correct, coordinates are assigned, shot is added
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1

        if check_if_hits(current_row, current_column, fleet):
            if not already_hit(current_row,current_column, fleet):
                print("Thats a hit!")
                print("\n")
                b.set_hit(current_row,current_column) # If hit, the location on the board is replaced with new symbol.
                b.show_board() # Board reprinted to reflect hit

                # Hit placed within the fleet and ship instance
                (fleet, ship_hit) = hit(current_row, current_column, fleet)
                if is_sunk(ship_hit):
                    ''' 
                    If the hit results in a sinking, the following block of code, takes a count of ships that are sunk and subtracts from amount at the start of the game.
                    Additionally, if a ship is sunk, the hit mark is changed from a * to the first letter of the ship type. Not just telling the user what was sank but also showing it.
                    '''
                    print("You sank a " + ship_type(ship_hit) + "!")

                    bs_count = 1
                    cr_count = 2
                    ds_count = 3
                    sm_count = 4

                    for ship in fleet:
                        if is_sunk(ship):
                            if ship_type(ship) == "battleship":
                                for coor in ship[4]:
                                    b.set_hit(coor[0],coor[1], "B ")
                                bs_count -= 1 
                            elif ship_type(ship) == "cruiser":
                                for coor in ship[4]:
                                    b.set_hit(coor[0],coor[1], "C ")
                                cr_count -= 1
                            elif ship_type(ship) == "destroyer":
                                for coor in ship[4]:
                                    b.set_hit(coor[0],coor[1], "D ")
                                ds_count -= 1
                            elif ship_type(ship) == "submarine":
                                for coor in ship[4]:
                                    b.set_hit(coor[0],coor[1], "S ")
                                sm_count -= 1 
                    print(f'You have {bs_count} battleship(s), {cr_count} cruiser(s), {ds_count} destroyer(s), {sm_count} submarine(s) remaining!')
                    # print_board(board)
                    b.show_board()

            else:
                # Code to run if the given coordinates are a hit but this area has already been hit
                shots -= 1
                print("You have already hit this area, please pick a new target!")

        else:

            if already_missed(current_row, current_column, missed):
                # If the user already has input these coordinates and missed, shot is removed and user is prompted. 
                shots -= 1
                print("You have already missed in this area, please pick a new target!")

            else:
                # If the shot is not a hit, the user is told that its a miss and a slash is given as a symbol.
                print("You missed!")
                print("\n")

                missed.add((current_row, current_column)) # Adds the missed coordinates to the missed set. 
                b.set_miss(current_row,current_column)
                b.show_board()


        if not are_unsunk_ships_left(fleet):
            # If all ships are sank, game is over. 
            game_over = True
            break

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
