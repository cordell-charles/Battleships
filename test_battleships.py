import pytest
from battleships import *

# Ship representation - (row, column, horizontal, length, hits) 

# Fleet - The fleet consists of 10 ships. The fleet is made up of 4 different types of ships, each of different size as follows: One battleship (4 squares), Two cruisers (3 squares), Three destroyers (2 squares), Four submarines (1 square).



# Checks if the input (row or column) is within the boundary of the board
def test_within_boundary1():

    # Example row or col input
    num = 4

    # Test case
    assert within_boundary(num) == True


def test_within_boundary2():
    # Example row or col input
    num = -1

    # Test case
    assert within_boundary(num) == False

def test_within_boundary3():
    # Example row or col input
    num = 12

    # Test case
    assert within_boundary(num) == False

def test_within_boundary4():
    # Example row or col input
    num = 0

    # Test case
    assert within_boundary(num) == True


def test_within_boundary5():
    # Example row or col input
    num = 9

    # Test case
    assert within_boundary(num) == True






# Is adjacent checking to see if given ship coordinates are adjacent to the given row and column at any point

def test_is_adjacent1():
    # ship coordinates instances:
    coor = (2,3)

    # test case
    assert is_adjacent(coor[0],coor[1], 1, 3) == True

def test_is_adjacent2():
    # ship coordinates instances:
    coor = (2,3)

    # test case
    assert is_adjacent(coor[0],coor[1], 6, 5) == False

def test_is_adjacent3():
    # ship coordinates instances:
    coor = (9,9)

    # test case
    assert is_adjacent(coor[0],coor[1], 9, 9) == False  # Not adjacent but ontop of, separate code will track these cases

def test_is_adjacent4():
    # ship coordinates instances:
    coor = (9,9)

    # test case
    assert is_adjacent(coor[0],coor[1], 8, 8) == True

def test_is_adjacent5():
    # ship coordinates instances:
    coor = (5,6)

    # test case
    assert is_adjacent(coor[0],coor[1], 6, 7) == True









# Test case checks to see if the any of the ships in a fleet have already been hit by the given row and column

def test_already_hit1():
    
    # Ship, fleet and coordinates for checking.
    ship1 = (5,5, True, 2,set())
    ship2 = (7,7, False, 2,{(7,7),(8,7)})
    ship3 = (1,7, True, 2,set())

    fleet = [ship1,ship2,ship3]
    coordinates = (2,2)


    # Test case
    assert already_hit(coordinates[0],coordinates[1],fleet) == False


def test_already_hit2():

    # Ship, fleet and coordinates for checking.
    ship1 = (5,5, True, 2,set())
    ship2 = (7,7, False, 2,{(7,7),(8,7)})
    ship3 = (1,7, True, 2,set())

    fleet = [ship1,ship2,ship3]
    coordinates = (8,7)


    # Test case
    assert already_hit(coordinates[0],coordinates[1],fleet) == True



def test_already_hit3():

    ship1 = (6,4, False, 1,{(6,4)})
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, False, 1,{(1,2)})

    fleet = [ship1,ship2,ship3]
    coordinates = (6,4)


    # Test case
    assert already_hit(coordinates[0],coordinates[1],fleet) == True

def test_already_hit4():

    ship1 = (6,4, False, 1,{(6,4)})
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, False, 2,{(1,2)})

    fleet = [ship1,ship2,ship3]
    coordinates = (8,8)


    # Test case
    assert already_hit(coordinates[0],coordinates[1],fleet) == False


def test_already_hit5():

    ship1 = (6,4, False, 1,{(6,4)})
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, True, 3,{(1,2),(1,4)})

    fleet = [ship1,ship2,ship3]
    coordinates = (1,3)


    # Test case
    assert already_hit(coordinates[0],coordinates[1],fleet) == False








def test_already_missed1():

    # A set of missed coordinates already used and coordinates
    missed = {(2,4),(5,5),(4,4),(9,8)}
    coor = (5,5)

    # Test case
    assert already_missed(coor[0],coor[1],missed) == True


def test_already_missed2():

    # A set of missed coordinates already used and coordinates
    missed = {(2,4),(5,5),(4,4),(9,8)}
    coor = (6,4)

    # Test case
    assert already_missed(coor[0],coor[1],missed) == False


def test_already_missed3():

    # A set of missed coordinates already used and coordinates
    missed = {(2,4),(5,5),(4,4),(9,8),(7,7),(9,2),(6,3)}
    coor = (0,0)

    # Test case
    assert already_missed(coor[0],coor[1],missed) == False


def test_already_missed4():

    # A set of missed coordinates already used and coordinates
    missed = {(2,4),(5,5),(4,4),(9,8),(7,7),(9,2),(6,3)}
    coor = (9,2)

    # Test case
    assert already_missed(coor[0],coor[1],missed) == True



def test_already_missed5():

    # A set of missed coordinates already used and coordinates
    missed = {(2,4),(5,5),(4,4),(9,8),(7,7),(9,2),(6,3)}
    coor = (4,4)

    # Test case
    assert already_missed(coor[0],coor[1],missed) == True










# Is sunk tests:
# If sunk returns true if the ship is sunk, false otherwise. 

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (2,4), (2,5)})
    assert is_sunk(s) == True

def test_is_sunk2():
    s = (2, 3, False, 3, {(2,3)})
    assert is_sunk(s) == False

def test_is_sunk3():
    s = (2, 3, False, 3, set())
    assert is_sunk(s) == False

def test_is_sunk4():
    s = (2, 3, True, 4, {(2,3), (3,3), (4,3), (5,3)})
    assert is_sunk(s) == True

def test_is_sunk5():
    s = (2, 3, True, 4, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == False






# Ship type tests:

# ship_type(ship) -- returns one of the strings "battleship", "cruiser", "destroyer", or "submarine" identifying the type of ship


def test_ship_type1():

    # Ship variables created
    w = (2,7, False, 1,set())

    # Test case:
    assert ship_type(w) == "submarine"


def test_ship_type2():
    x = (6,5, False, 2,set())
    assert ship_type(x) == "destroyer"

def test_ship_type3():
    y = (9,2, True, 3,set())
    assert ship_type(y) == "cruiser"

def test_ship_type4():
    z = (4,4, True, 4,set())
    assert ship_type(z) == "battleship"

def test_ship_type5():
    # 'no_ship = ' Variable to test if incorrect ship format added
    not_ship = 4,5,False, 45, set() == 'Not ship type, please try again'








#Open seas test: 

# is_open_sea(row, column, fleet) -- checks if the square given by row and column neither contains nor is adjacent (horizontally, vertically, or diagonally) to some ship in fleet. Returns Boolean True if so and False otherwise.


def test_is_open_sea1():

    # Ship creation to add to fleet list
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    ship3 = (9,2, True, 3,set())

    # arguments created for open sea function
    row = 5
    column = 6
    fleet = [ship1, ship2, ship3]

    # test case
    assert is_open_sea(row,column, fleet) == False


def test_is_open_sea2():

    # Ship creation to add to fleet list
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    ship3 = (9,2, True, 3,set())

    # arguments created for open sea function
    row = 0
    column = 9
    fleet = [ship1, ship2, ship3]

    # test case
    assert is_open_sea(row,column, fleet) == True


def test_is_open_sea3():

    # Ship creation to add to fleet list
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    ship3 = (9,2, True, 3,set())

    # arguments created for open sea function
    row = 1
    column = 6
    fleet = [ship1, ship2, ship3]

    # test case
    assert is_open_sea(row,column, fleet) == False

def test_is_open_sea4():

    # Ship creation to add to fleet list
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    ship3 = (9,2, True, 3,set())

    # arguments created for open sea function
    row = 9
    column = 9
    fleet = [ship1, ship2, ship3]

    # test case
    assert is_open_sea(row,column, fleet) == True


def test_is_open_sea5():

    # Ship creation to add to fleet list
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    ship3 = (9,2, True, 3,set())

    # arguments created for open sea function
    row = 6
    column = 6
    fleet = [ship1, ship2, ship3]

    # test case
    assert is_open_sea(row,column, fleet) == False












# Ok to place ships test:

# ok_to_place_ship_at(row, column, horizontal, length, fleet)-- checks if addition of a ship, specified by row, column, horizontal, and length as in ship representation above, to the fleet results in a legal arrangement (see the figure above). If so, the function returns Boolean True and it returns False otherwise. This function makes use of the function is_open_sea


def test_ok_to_place_ship_at1():

    # Ships and fleet:
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    fleet = [ship1, ship2]
    
    # Test case:
    assert ok_to_place_ship_at(8,6,True, 2, fleet) == False


def test_ok_to_place_ship_at2():

    # Ships and fleet:
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    fleet = [ship1, ship2]
  
    # Test case:
    assert ok_to_place_ship_at(6,5, False, 3, fleet) == False



def test_ok_to_place_ship_at3():

    # Ships and fleet:
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    fleet = [ship1, ship2]
  
    # Test case:
    assert ok_to_place_ship_at(13,5, False, 3, fleet) == "Row input out of bounds!"


def test_ok_to_place_ship_at4():

    # Ships and fleet:
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    fleet = [ship1, ship2]
  
    # Test case:
    assert ok_to_place_ship_at(6,-1, False, 3, fleet) == "Column input out of bounds!"


def test_ok_to_place_ship_at5():

    # Full ship and fleet instance
    ship1 = (4,5, False, 1,set())
    ship2 = (3,4, True, 1,set())
    ship3 = (1,2, False, 1,set())
    ship4 = (2,9, False, 1,set())
    ship5 = (5,5, True, 2,set())
    ship6 = (7,7, False, 2,{(6,7),(7,7)})
    ship7 = (1,7, True, 2,set())
    ship8 = (9,6, True, 3,set())
    ship9 = (7,5, False, 3,{(6,7)})


    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]


    # Test case:
    assert ok_to_place_ship_at(3,7, False, 4, fleet) == True












# Place ships test 

# place_ship_at(row, column, horizontal, length, fleet) -- returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, and length as in ship representation above, to fleet. It may be assumed that the resulting arrangement of the new fleet is legal


def test_place_ship_at1():

    # Ships to add to fleet
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())
    ship3 = (8,3, True, 4,set())

    # fleet cases
    fleet = [ship1, ship2]
    fleet2 = [ship1, ship2, ship3]

    # Test case upon passing ship3 through place ship, the result should return True and == fleet2
    assert place_ship_at(8,3,True,4,fleet) == fleet2  # Return True


def test_place_ship_at2():

    # Ships to add to fleet
    ship1 = (2,7, False, 1,set())
    ship2 = (6,5, False, 2,set())

    # fleet cases
    fleet = [ship1, ship2]

    # Test case 
    assert place_ship_at(8,3,True,4,fleet) == fleet 



def test_place_ship_at3():

    # Ships to add to fleet
    ship1 = (4,5, False, 1,set())
    ship2 = (3,4, True, 1,set())
    ship3 = (1,2, False, 1,set())
    ship4 = (2,9, False, 1,set())
    ship5 = (5,5, True, 2,set())
    ship6 = (7,7, False, 2,set())
    ship7 = (1,7, True, 2,set())
    ship8 = (9,6, True, 3,set())
    ship9 = (1,9,False,3,set())

    # fleet cases
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8]
    fleet2 = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]

    # Test case
    assert place_ship_at(1,9,False,3,fleet) == fleet2  # Return True



def test_place_ship_at4():
    # Ships to add to fleet
    ship1 = (4,5, False, 1,set())
    ship2 = (3,4, True, 1,set())
    ship3 = (1,2, False, 1,set())
    ship4 = (2,9, False, 1,set())
    ship5 = (5,5, True, 2,set())
    ship6 = (7,7, False, 2,set())
    ship7 = (1,7, True, 2,set())
    ship8 = (9,6, True, 3,set())
    ship9 = (1,9,False,3,set())
    ship10 = (9,2, True, 1, set())

    # fleet cases
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    fleet2 = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]

    # Test case
    assert place_ship_at(9,2,True,1,fleet) == fleet2  

def test_place_ship_at5():

    ship1 = (2,7, False, 1,set())
    ship2 = (8,5, False, 4,set())

    # fleet cases
    fleet = [ship1]
    fleet2 = [ship1, ship2]

    # Test case
    assert place_ship_at(8,5,False,4,fleet) == fleet2  











# Check if hit tests

# check_if_hits(row, column, fleet) -- returns Boolean value, which is True if the shot of the human player at the square represented by row and column hits any of the ships of fleet, and False otherwise


def test_check_if_hits1():

    # Ships & fleet
    ship1 = (2,7, False, 2,set())
    ship2 = (6,5, False, 3,set())
    ship3 = (8,3, True, 4,set())
    fleet = [ship1, ship2, ship3]

    # Test case
    assert check_if_hits(7, 5, fleet) == True


def test_check_if_hits2():

    # Ships & fleet
    ship1 = (2,8, False, 4,set())
    ship2 = (2,4, False, 3,set())
    ship3 = (6,3, True, 4,set())
    fleet = [ship1, ship2, ship3]

    # Test case
    assert check_if_hits(9,1,fleet) == False

def test_check_if_hits3():


    # Ships & fleet
    ship1 = (2,8, False, 4,set())
    ship2 = (2,4, False, 3, {(2,4),(2,5),(2,6)})
    ship3 = (6,3, True, 4,set())
    fleet = [ship1, ship2, ship3]

    # Test case
    assert check_if_hits(9,9,fleet) == False


def test_check_if_hits4():

    # Full ship instance
    ship1 = (8,8, False, 1,{(8,8)})
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, False, 1,{(1,2)})
    ship4 = (2,9, False, 1,{(2,9)})
    ship5 = (5,5, True, 2,{(5,5), (6,5)})
    ship6 = (7,7, False, 2,{(7,7), (8,7)})
    ship7 = (1,7, True, 2,{(1,7), (1,8)})
    ship8 = (9,1, True, 3,{(9,1), (9,2)})


    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8]

    # Test case
    assert check_if_hits(9,3,fleet) == True



def test_check_if_hits5():

    # Ships & fleet
    ship1 = (2,8, False, 4,set())
    ship2 = (2,4, False, 3, {(2,4),(2,5),(2,6)})
    ship3 = (6,3, True, 4,set())
    fleet = [ship1, ship2, ship3]

    # Test case
    assert check_if_hits(6,6,fleet) == True














# Hit ships tests

# hit(row, column, fleet) -- returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that receives a hit by the shot at the square represented by row and column, and fleet1 is the fleet resulting from this hit. It may be assumed that shooting at the square row, column results in of some ship in fleet


def test_hit1():

    # ship instance
    ship1 = (7,5, False, 3,set())
    ship2 = (4,9, False, 4,set())
    ship3 = (4,9, False, 4,{(4,9)})

    # Fleet instance:
    fleet = [ship1, ship2]
    fleet_update = [ship1, ship3]


    # Test case:
    assert hit(4, 9, fleet) == (fleet_update, ship3)



def test_hit2():
    # ship instance
    ship1 = (7,5, True, 3,set())
    ship2 = (4,9, False, 4,{(4,9)})
    ship3 = (4,9, False, 4,{(4,9), (6,9)})

    # Fleet instance:
    fleet = [ship1, ship2]
    fleet_update = [ship1, ship3]


    # Test case:
    assert hit(6, 9, fleet) == (fleet_update, ship3)



def test_hit3():

    # ship instance
    ship1 = (7,5, False, 3,set())
    ship2 = (4,2, True, 4,{(4,2), (4,3)})
    ship3 = (4,2, True, 4,{(4,2),(4,3),(4,4)})

    # Fleet instance:
    fleet = [ship1, ship2]
    fleet_update = [ship1, ship3]


    # Test case:
    assert hit(4, 4, fleet) == (fleet_update, ship3)



def test_hit4():

    # ship instance
    ship1 = (7,5, False, 3,set())
    ship2 = (9,1, True, 4,{(9,1)})
    ship3 = (9,1, True, 4,{(9,1),(9,4)})

    # Fleet instance:
    fleet = [ship1, ship2]
    fleet_update = [ship1, ship3]


    # Test case:
    assert hit(9, 4, fleet) == (fleet_update, ship3) 





def test_hit5():

    # ship instance
    ship1 = (7,5, False, 3,set())
    ship2 = (4,9, True, 4,{(4,9),(6,9), (5,9)})
    
    ship3 = (7,5, False, 3, {(7,5)})
    ship4 = (4,9, True, 4,{(4,9),(6,9), (5,9)})

    # Fleet instance:
    fleet = [ship1, ship2]
    fleet_update = [ship3, ship4]


    # Test case:
    assert hit(7, 5, fleet) == (fleet_update, ship3)











# Unsunk ships test

# are_unsunk_ships_left(fleet) -- returns Boolean value, which is True if there are ships in the fleet that are still not sunk, and False otherwise

def test_are_unsunk_ships_left1():

    # Full ship instance
    ship1 = (8,8, False, 1,set())
    ship2 = (3,4, True, 1,set())
    ship3 = (1,2, False, 1,set())
    ship4 = (2,9, False, 1,set())
    ship5 = (5,5, True, 2,set())
    ship6 = (7,7, False, 2,set())
    ship7 = (1,7, True, 2,set())
    ship8 = (9,6, True, 3,set())
    ship9 = (7,5, False, 3,set())
    ship10 = (4,9, False, 4,set())

    # Fleet instance:
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9 ,ship10]


    # Test case
    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left2():

    # Full ship instance
    ship1 = (8,8, False, 1,{(8,8)})
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, False, 1,{(1,2)})
    ship4 = (2,9, False, 1,{(2,9)})
    ship5 = (5,5, True, 2,{(5,5), (6,5)})
    ship6 = (7,7, False, 2,{(7,7), (8,7)})
    ship7 = (1,7, True, 2,{(1,7), (1,8)})
    ship8 = (9,1, True, 3,{(9,1), (9,2), (9,3)})
    ship9 = (7,5, False, 3,{(7,5), (8,5), (9,5)})
    ship10 = (4,9, False, 4,{(4,9), (5,9), (6,9), (7,9)})

    # Fleet instance:
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9 ,ship10]

    #Test case
    assert are_unsunk_ships_left(fleet) == False
    


def test_are_unsunk_ships_left3():

    # Full ship instance, some sunk, others just hit
    ship1 = (8,8, False, 1,set())
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, False, 1,set())
    ship4 = (2,9, False, 1,set())
    ship5 = (5,5, True, 2,{(5,5)})
    ship6 = (7,7, False, 2,set())
    ship7 = (1,7, True, 2,set())
    ship8 = (9,6, True, 3,set())
    ship9 = (7,5, False, 3,{(7,5), (8,5), (9,5)})
    ship10 = (4,9, False, 4,{(4,9), (5,9)})

    # Fleet instance:
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9 ,ship10]

    # Test case:
    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left4():

    # Full ship instance
    ship1 = (8,8, False, 1,{(8,8)})
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, False, 2,{(1,2)})


    # Fleet instance:
    fleet = [ship1, ship2, ship3]

    #Test case
    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left5():
    # Full ship instance
    ship1 = (8,8, False, 1,{(8,8)})
    ship2 = (3,4, True, 1,{(3,4)})
    ship3 = (1,2, False, 2,{(1,2), (1,3)})


    # Fleet instance:
    fleet = [ship1, ship2, ship3]

    #Test case
    assert are_unsunk_ships_left(fleet) == False
    
