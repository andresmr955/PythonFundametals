from player import Player

class BattleshipGame:
    """
    Represents a Battleship game with two players.

    Initializes two Player objects to simulate the game between them.
    """

    def __init__(self):
        """
        Initializes the BattleshipGame by creating two players:
        - Player one (e.g., the user)
        - Player two (e.g., the computer or another opponent)
        """
        self.player_one = Player("Andres")
        self.player_two = Player("Jose")
    
    def play(self):

        print('*' * 40)
        print('*' * 40)
        print("Welcome to Battle Ship")
        print('*' * 40)
        
        print(f"The first player {self.player_one.name} and he is going to place his ships")
        print('*' * 40)
        
        self.player_one.place_ships()
        print('*' * 40)
        print(f"The second player {self.player_two.name} is going to place his ships")
        print('*' * 40)
        self.player_two.place_ships()

        current_player = self.player_one
        opponent = self.player_two

        while True:
            print('*' * 40)
            current_player.attack(opponent)
            print('*' * 40)

            if current_player.attack(opponent):
                if opponent.all_ships_sunk():
                    print(f'\n{current_player.name} wins! All enemy ships have been sunk')
                    break
            
            current_player, opponent = opponent, current_player
            
           
            
                
battleinstance = BattleshipGame()

battleinstance.play()