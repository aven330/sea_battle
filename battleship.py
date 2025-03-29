import time
def delayed_type(word, delay):
        """
        Prints word letter by letter
        ---
        Parameters:
            word (str): word to type letter by letter
            delay (float): delay between each letter
        ---
        Returns:
            None
        """
        for letter in word:
            time.sleep(delay)
            print(letter, end = "", flush = True)
        print()
class Player:
    """
    BATTLESHIP GAME ON TERMINAL
    """
    def __init__(self):
        """
        Constructor of Player.
        
        Initializes the specified attributes on creation:
        - name (str): name of player.
        - fleet (dict): dictionary filled with ships names as keys and a list
        that contains the ship as values.
        - fleet_locations (dict): initially empty and as ships are created,
        their list index is saved as a list
        - misses (non-negative int): number of missses a player has made
        - hits (non-negative int): number of hits a player has made
        - sinks (non-negative int): number of ships a player has destroyed
        - x_axis (list): the x-axis of the gameboard
        - y_axis (list): the y-axis of the gameboard
        - rows (list): the empty spots of the gameboard
        - board (list): gameboard
        - guess_board (list): blank version of the board so player can track
        guesses
        """       
        delayed_type('PLAYER NAME', .01)
        self.name = input()
        self.fleet = {'SHIP_ONE': ['◀', '◀'],
    'SHIP_TWO': ['◀', '◀', '◀'],
    'SHIP_THREE': ['◀', '◀', '◀'],  
    'SHIP_FOUR': ['◀', '◀', '◀', '◀'],
    'SHIP_FIVE':  ['◀', '◀', '◀', '◀', '◀']}
        self.fleet_locations = {}
        self.ship_status = {k: 'ONLINE' for k in self.fleet}
        self.misses = 0
        self.hits = 0
        self.sinks = 0
        self.x_axis = ['+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.y_axis = [str(i) for i in range(1,11)]
        self.rows = ['_' for i in range(10)]
        self.board = [self.x_axis] + [[self.y_axis[i]]+ self.rows for i in range(len(self.y_axis))]
        self.guess_board = [self.x_axis] + [[self.y_axis[i]]+ self.rows for i in range(len(self.y_axis))]
    def display_board(self):
        """
        Prints a visually friendly version of the board
        ---
        Parameters:
            None
        ---
        Returns:
            None
        """  
        printable_board = ["  ".join(i) for i in self.board]
        printable_board[-1] = '10 _  _  _  _  _  _  _  _  _  _'
        for i in printable_board:
            time.sleep(.05)
            print(i)
    def display_guess_board(self):
        """
        Prints a visually friendly version of the guess board
        ---
        Parameters:
            None
        ---
        Returns:
            None
        """ 
        printable__guess_board = ["  ".join(i) for i in self.guess_board]
        printable__guess_board[-1] = '10 _  _  _  _  _  _  _  _  _  _'
        for i in printable__guess_board:
            time.sleep(.05)
            print(i)

    def set_ship(self, ship, coordinate, orientation):
        """
        Sets an individual ship given a coordinate of the head of the ship
        and an orientation
        ---
        Parameters:
            ship (str): name of ship to set
            coordinate (str): coordinates of the ship given by the get_coords
            function
            orientation (str): whether or not the ship is horizontal or
            vertical
        ---
        Returns:
            None
        """ 
        try:
            x = self.x_axis.index(coordinate[0].upper())
            y = int(coordinate[1:])
            ship_length = len(self.fleet[ship])
            if orientation[0].lower() == 'h':
                if x+ship_length > len(self.board[y]):
                    raise IndexError()
                if '◀' in self.board[y][x:(x+ship_length)] or '▼' in self.board[y][x:(x+ship_length)]:
                    delayed_type("SHIP ALREADY THERE! CHOOSE AGAIN!", .01)
                    self.get_coords(ship)
                else:
                    self.board[y][x:(x+ship_length)] = self.fleet[ship]
                    self.fleet_locations[ship] = [y, [x, x+ship_length]]
                    self.display_board()
                    delayed_type(f"{ship} SET!", .01)
            if orientation[0].lower() == 'v':
                if y+ship_length > len(self.board):
                    raise IndexError()
                if '▼' in [self.board[y+h][x] for h in range(ship_length)] or '◀' in [self.board[y+h][x] for h in range(ship_length)]:
                    delayed_type("SHIP ALREADY THERE! CHOOSE AGAIN!", .01)
                    self.get_coords(ship)
                else:
                    for i in range(ship_length):
                        self.board[y+i][x] = '▼'
                    self.fleet_locations[ship] = [[y, y+ship_length], x]
                self.display_board()
                delayed_type(f"{ship} SET!", .01)
        except(IndexError):
            delayed_type('OUT OF BOUNDS! INPUT NEW COORDINATES!', .01)
            self.get_coords(ship)
    def get_coords(self, ship):
        """
        Ask's the player for the coordinates and orientation of the ship they
        want to place
        ---
        Parameters:
            ship (str): name of ship to set
        ---
        Returns:
            None
        """ 
        delayed_type("COORDINATES?", .01)
        coordinate = input()
        while (coordinate == '') or (coordinate[0].upper() not in self.x_axis) or (coordinate[1:] not in self.y_axis):
            delayed_type("COORDINATES DO NOT EXIST! TRY AGAIN", .01)
            coordinate = input()
        delayed_type("ORIENTATION?", .01)
        orientation = input()
        while (orientation.lower() != 'h' and orientation.lower() != 'v'):
            delayed_type("ORIENTATION IS EITHER HORIZONTAL OR VERTICAL", .01)
            orientation = input()
        self.set_ship(ship, coordinate, orientation)

    def set_fleet(self):
        """
        Sets the entire fleet using the set ship function
        ---
        Parameters:
            ship (str): name of ship to set
            coordinate (str): coordinates of the ship 
            orientation (str): whether or not the ship is horizontal or
            vertical
        ---
        Returns:
            None
        """ 
        delayed_type(f"{self.name.upper()} PLAN YOUR FLEET!", .01)
        self.display_board()
        for i in self.fleet:
            self.get_coords(i)
        delayed_type("ALL SET!", .01)
        self.display_board()
        for i in range(25):
            print('.\n')

    def battle(self, other_ship):
        """
        Starts the battle between 2 players
        ---
        Parameters:
            other_ship (object): enemy ship object
        ---
        Returns:
            None
        """ 
        for i in range(25):
            print('.\n')
        delayed_type("GET READY TO BATTLE!", .01)
        while self.sinks < 5 and other_ship.sinks < 5:
            for player, opponent in [(self, other_ship), (other_ship, self)]:
                delayed_type(f"{player.name}'S TURN", .01)
                player.display_guess_board()
                hit = True
                while hit:
                    hit = player.targeting(opponent)
                    if self.sinks == 5:
                        hit = False
                if player.sinks == 5:
                    delayed_type(f"{player.name} HAS WON!!!", .01)
                    self.reveal_boards()
                    other_ship.reveal_boards()
                    return

    def targeting(self, other_ship):
        """
        Handles the guessing done by each player as well as updates the guess
        board and enemy ships board
        ---
        Parameters:
            other_ship (object): enemy ship object
        ---
        Returns:
            True if hit and False if miss.
        """ 
        delayed_type(f"CHOOSE YOUR TARGET {self.name}", .01)
        target = input()
        while (target[0].upper() not in self.x_axis) or (target[1:] not in self.y_axis):
            delayed_type("TARGET DOES NOT EXIST! TRY AGAIN", .01)
            target = input()
        x = self.x_axis.index(target[0].upper())
        y = int(target[1:])
        if other_ship.board[y][x] == '◀' or other_ship.board[y][x] == '▼':
            self.guess_board[y][x] = 'X'
            self.hits += 1
            other_ship.board[y][x] = 'X'
            delayed_type("HIT!", .01)
            self.display_guess_board()
            self.check_status(other_ship)
            return True
        elif other_ship.board[y][x] == '_':
            self.guess_board[y][x] = 'O'
            self.misses += 1
            other_ship.board[y][x] = 'O'
            delayed_type("MISS!", .01)
            self.display_guess_board()
            self.check_status(other_ship)
            return False
        else:
            delayed_type("ALREADY HIT! TRY AGAIN", .01)
            self.targeting(other_ship)

    def check_status(self, other_ship):
        """
        Updates every ship with current hits and sees if a ship has sinked and
        updates ship_status with dead ships and updates the fleet with ship
        hits
        ---
        Parameters:
            other_ship (object): enemy ship object
        ---
        Returns:
            None
        """ 
        for i in other_ship.fleet_locations:
            ship = other_ship.fleet_locations[i]
            ship_vertical = isinstance(ship[0], list)
            ship_horizontal = isinstance(ship[1], list)
            if ship_vertical:
                other_ship.fleet[i] = [other_ship.board[ship[0][0]+i][ship[1]] for i in range(len(self.fleet[i]))]
            if ship_horizontal:
                other_ship.fleet[i] = other_ship.board[ship[0]][ship[1][0]:ship[1][1]]
            if all('X' == integrity for integrity in other_ship.fleet[i]) and other_ship.ship_status[i] != 'OFFLINE!':
                self.sinks += 1
                other_ship.ship_status[i] = 'OFFLINE!'
                delayed_type(f"YOU SUNK {i}!!", .01)
    def reveal_boards(self):
        """
        Reveals both players boards after the game has ended
        ---
        Parameters:
            None
        ---
        Returns:
            None
        """ 
        delayed_type(f"{self.name.upper()}'S BOARD", .05)
        self.display_board()
                    

# Runs the game
delayed_type("LETS PLAY BATTLESHIP!", .01)
# Creates Player 1 Object
p1 = Player()
# Creates Player 2 Object
p2 = Player()
# Sets Player 1's ships
p1.set_fleet()
# Sets Player 2's ships
p2.set_fleet()
# Starts the game
p1.battle(p2)



