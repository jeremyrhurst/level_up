# Snake game
# move (up, left, right, down)
# snake initial size = 3
# snake grows by 1 segment every 5 moves

class Snake():
    def __init__(self):
        self.game_board = [
            ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            ]
        self.moves_since_grow = 0
        self.snake = [[0,0], [0,1], [0,2]]
       
       
    # Each move:
           # if move_since_grow is greater than 5:
           # append to snake new head coordinate
           # otherwise:
           # Set new head, and set all following coords of snake to neighbor
           # Update tail on board to ' '
                 
         #
   
    def move(self, direction):
        directions = {'up': (-1, 0), 'right': (0, 1)}
        # Move in that direction
        self.snake[-1][0] += directions[direction][0]
        if self.snake[-1][0] > 9:
            self.snake[-1][0] = 0
        if self.snake[-1][0] < 0:
            self.snake[-1][0] = 9
        self.snake[-1][1] += directions[direction][1]
        if self.snake[-1][1] > 9:
            self.snake[-1][1] = 0
        if self.snake[-1][1] < 0:
            self.snake[-1][1] = 9
        if self.game_board[self.snake[-1][0]][self.snake[-1][1]] == '#':
            print('You died!')
            return
       
        self.game_board[self.snake[-1][0]][self.snake[-1][1]] = '#'
        if self.moves_since_grow < 5:
            self.game_board[self.snake[0][0]][self.snake[0][1]] = ' '
        self.moves_since_grow += 1
           
       
       
       
       
       
        # Increase moves since grow
        # Add to tail if moves greater than 5
       
       
game = Snake()
print(game.game_board)
game.move('right')
print(game.game_board)
game.move('right')
print(game.game_board)
game.move('right')
print(game.game_board)
game.move('right')
print(game.game_board