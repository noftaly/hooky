import pygame as pg
from utils import BlockType
from vector import Vector

class Edge:
	def __init__(self, first, second):
		self.first_point = first
		self.second_point = second

class Block:
	# location is the top-left location
	def __init__(self, location, game, block_type):
		self.pos = Vector(location.x * 64, location.y * 64)
		self.cell = Vector(location.x, location.y)
		self.game = game

		self.type = block_type
		top_left = Vector(self.pos.x, self.pos.y)
		top_right = Vector(self.pos.x, self.pos.y + game.CELL_SIZE)
		bottom_left = Vector(self.pos.x - game.CELL_SIZE, self.pos.y)
		bottom_right = Vector(self.pos.x - game.CELL_SIZE, self.pos.y + game.CELL_SIZE)
		self.left = Edge(bottom_left, top_left)
		self.right = Edge(bottom_right, top_right)
		self.top = Edge(top_left, top_right)
		self.bottom = Edge(bottom_left, bottom_right)

	def display(self):
		print(self)
		color = (120, 180, 255)
		if self.type == 1:
			color = (100, 60, 30)

		pg.draw.rect(
			self.game.surface,
			color,
			(
				self.pos.x - self.game.player.pos.x + self.game.half_size[0],
				self.pos.y - self.game.player.pos.y + self.game.half_size[1],
				self.game.CELL_SIZE,
				self.game.CELL_SIZE
			)
		)

	def __str__(self):
		return f'Block {self.type} {self.pos}'

	def __repr__(self):
		return f'Block {self.type} {self.pos}'
