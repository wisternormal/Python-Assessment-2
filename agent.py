import random


class Agent(object):

	"""docstring for Agent"""

	def __init__(self):
		self.x = 136
		self.y = 148

	def move(self):
		# need to adjust the Step value
		Step = 3
		if random.random() < 0.5:
			self.y = self.y + Step
		else:
			self.y = self.y - Step
		
		if random.random() < 0.5:
			self.x = self.x + Step
		else:
			self.x = self.x - Step

		if self.x < 20:
			self.x = self.x + Step
		if self.x > 270:
			self.x = self.x - Step

		if self.y < 20:
			self.y = self.y + Step
		if self.y > 270:
			self.y = self.y - Step