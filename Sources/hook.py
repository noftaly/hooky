from entity import Entity

class Hook(Entity):
	def __init__(self, player, game):
		super().__init__(player.pos, game, 1)

		self.player = player
		self.game = game
		self.visible = False
	
	def launch():
		pass
