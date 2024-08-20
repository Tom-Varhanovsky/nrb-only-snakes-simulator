#Simulator of Snakes and Ladders - but ONLY SNAKES based on a video by No Rolls Barred
from random import randint

class Player:
    def __init__(self):
        self.position = 0
        self.steps_on_snakes = 0

class Game:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.board = self.setup_board()
        self.player1 = Player()
        self.player2 = Player()
        self.current_player = 1
        self.current_turn = 1

    @staticmethod
    def setup_board():
        rows, cols = (10, 10)

        board = [[0]*cols for _ in range(rows)]

        return board


    def add_snake(self, head, tail):
        head_coordinates = self.position_converter(head)
        self.board[head_coordinates[0]][head_coordinates[1]] = tail

    def add_default_snakes(self):
        self.add_snake(14,4)
        self.add_snake(17,7)
        self.add_snake(31,9)
        self.add_snake(38,20)
        self.add_snake(54,34)
        self.add_snake(59,40)
        self.add_snake(62,19)
        self.add_snake(64,60)
        self.add_snake(67,51)
        self.add_snake(81,63)
        self.add_snake(84,28)
        self.add_snake(87,24)
        self.add_snake(91,71)
        self.add_snake(93,73)
        self.add_snake(95,75)
        self.add_snake(99,78)


    @staticmethod
    def position_converter(position):
        coordinates = (position//10, (position%10)-1)
        return coordinates

    def print_board(self):
        for n in range(self.rows):
            print(self.board[n])

    def play(self):
        while self.player1.position != 100 and self.player2.position != 100:
            self.current_player = 1
            if self.play_turn_player(self.player1):
                break
            self.current_player = 2
            if self.play_turn_player(self.player2):
                break
            self.current_turn += 1
        print("Player " + str(self.current_player) + " wins!")
        print("There were " + str(self.current_turn) + " turns")
        print("Player 1 has stepped on snake " + str(self.player1.steps_on_snakes) + " times")
        print("Player 2 has stepped on snake " + str(self.player2.steps_on_snakes) + " times")
        return self.current_turn, self.player1.steps_on_snakes, self.player2.steps_on_snakes


    def play_turn_player(self, player):
        if player.position == 0:
            if self.current_turn == 1:
                for i in range(2):
                    if randint(1,6) == 6:
                        player.position = 1
            else:
                if randint(1, 6) == 6:
                    player.position = 1
        else:
            temp_position = player.position + randint(1, 6)
            if temp_position == 100:
                player.position = 100
                return True
            if temp_position > 100:
                temp_position = 100 - (temp_position - 100)
            temp_coordinates = self.position_converter(temp_position)
            if self.board[temp_coordinates[0]][temp_coordinates[1]] != 0:
                player.steps_on_snakes += 1
                player.position = self.board[temp_coordinates[0]][temp_coordinates[1]]
            else:
                player.position = temp_position
        return False
    def reset_game(self):
        self.player1.position = 0
        self.player1.steps_on_snakes = 0
        self.player2.position = 0
        self.player2.steps_on_snakes = 0
        self.current_turn = 0

def main():
    print("Simulator of Snakes and Ladders - but ONLY SNAKES based on a video by No Rolls Barred")

    
    new_game = Game()
    new_game.add_default_snakes()
    sum_values = (0, 0, 0)
    for i in range(1000):
        temp_tuple = new_game.play()
        sum_values = tuple(map(sum, zip(sum_values, temp_tuple)))
        new_game.reset_game()
    print_statistics(sum_values, 1000)

    print("END")

def print_statistics(sum_values, number_of_games):
    print("Game on average took " + str(sum_values[0]/number_of_games) + " turns")
    print("Player 1 stepped on snake average " + str(sum_values[1]/number_of_games) + " times")
    print("Player 2 stepped on snake average " + str(sum_values[2]/number_of_games) + " times")

if __name__ == "__main__":
    main()