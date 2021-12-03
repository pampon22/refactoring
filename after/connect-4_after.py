'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''

import turtle

class Draw:
	
	def __init__(self, num_rows, num_cols):
		self.window = None
		self.turt = None
		self.grid = []
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.tile_size = 50
		self.x_offset = -150
		self.y_offset = 200

	def get_window(self):
		return self.window

	def get_turt(self):
		return self.turt

	def get_grid(self):
		return self.grid

	def get_tile_size(self):
		return self.tile_size

	def make_window(self, window_title, bgcolor, dimensions):
		''' this function creates a screen object and returns it '''

		window = turtle.getscreen() # Set the window size
		window.title(window_title)
		window.bgcolor(bgcolor)
		window.setup(dimensions["width"], dimensions["height"])
		window.tracer(0) #turns off screen updates for the window Speeds up the game
		self.window = window

	def make_turtle(self, shape, color, stretch_param, point):
		''' creates a turtle and sets initial position '''

		turt = turtle.Turtle()
		turt.speed(0)    # Speed of animation, 0 is max
		turt.shape(shape)
		turt.color(color)
		turt.shapesize(stretch_param["stretch_width"], stretch_param["stretch_length"]) 
		turt.penup()
		turt.goto(point["x"], point["y"]) # Start position
		self.turt = turt

	def move_to(self, point):
		self.turt.up()
		self.turt.goto(point["x"], point["y"])
		self.turt.down()

	def draw_grid(self, point, tile_size):
		''' draws a grid at x, y with a specific tile_size '''

		self.move_to(point)

		self.tile_size = tile_size
		
		for row in range(len(self.grid)):
			for col in range(len(self.grid[row])):
				new_point = { "x": point["x"] + col * self.tile, "y": point["y"] -row *self.tile_size}
				self.move_to(new_point["x"], new_point["y"])

				if self.grid[row][col] == 1:
					self.turt.dot(self.tile_size-5, "red")
				
				elif self.grid[row][col] == 2:
					self.turt.dot(self.tile_size-5, "yellow")
				
				else:
					self.turt.dot(tile_size-5, "white")


class Game(Draw):
	
	def __init__(self, num_rows, num_cols):
		Draw.__init__(self, num_rows, num_cols)
		self.x_offset = -150
		self.y_offset = 200
		self.turn = True
		self.grid = []

	def check_rows(self, player):
		# checks rows
		count = 0

		for row in range(len(self.grid)):
			count = 0
			for col in range(len(self.grid[0])):
				if self.grid[row][col] == player:
					count += 1

					if count == 4:
						return True
				else:
					count = 0
				
	def check_columns(self, player):
		# check columns
		for col in range(len(self.grid[0])):
			count = 0
			for row in range(len(self.grid)):
				if self.grid[row][col] == player:
					count += 1
					
					if count == 4:
						return True
				else:
					count = 0

	def check_diagonal(self):
		# checks diagonal
		for row in range(len(self.grid)):
			for col in range(len(self.grid[0])):

				if row + 3 < len(self.grid) and col + 3 < len(self.grid[row]):
					if self.grid[row][col] == 1\
					and self.grid[row+1][col+1] == 1\
					and self.grid[row+2][col+2] == 1\
					and self.grid[row+3][col+3] == 1:
						return True 

	def check_winner(self, grid, player):
		''' checks the winner in the grid
		returns true if player won
		returns false if player lost
		'''
		if self.check_rows(player):
			return True
		elif self.check_columns(player):
			return True
		elif self.check_diagonal():
			return True
		else:
			return False


	def play(self, point):
		''' '''
		row = int(abs((point["y"] - self.y_offset - 25) // (50) + 1))
		col = int(abs((point["x"] - self.x_offset - 25) // (50) + 1))
		print(row, col)
		self.grid[row][col] = self.turn
		self.draw_grid({"x":self.x_offset, "y":self.y_offset}, self.get_tile_size())
		self.window.update()

		if self.check_winner(self.grid, 1):
			print("player 1 won")

		elif self.check_winner(self.grid, 2):
			print("player 2 won")

		if self.turn == 1:
			self.turn = 2
		else:
			self.turn = 1


	def initialize(self):
		self.window.onscreenclick(self.play)
		self.window.listen()

def main():
	''' the main function where the game events take place '''

	my_game = Game(5, 7)
	my_game.make_window("Connect 4", "light sky blue", {"width":800, "height":600})  
	my_game.make_turtle('classic', "white", {"stretch_width":1, "stretch_length":1}, {"x":0, "y":0})
	
	grid = my_game.get_grid()
	window = my_game.get_window()

	my_game.draw_grid({"x":my_game.x_offset, "y":my_game.y_offset}, my_game.get_tile_size())
	
	my_game.initialize()

	while True:
		selected_row = int(input("enter row, player "+ str(my_game.turn) +": "))
		selected_col = int(input("enter col, player "+ str(my_game.turn) +": "))

		if grid[selected_row][selected_col] == 0:

			if my_game.turn == 1:
				grid[selected_row][selected_col] = 1
			else:
				grid[selected_row][selected_col] = 2

		my_game.draw_grid({"x":-150, "y":200}, 50)
		window.update()


if __name__ == "__main__":
	main()

