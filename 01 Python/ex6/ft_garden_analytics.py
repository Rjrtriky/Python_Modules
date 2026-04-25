# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/26 01:27:36 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/26 01:27:40 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#=== PLANT CLASS ===
class Plant:
	#===STATISTICS CLASS===
	class Statistic:
		def __init__(self):
			self.n_grow = 0
			self.n_age = 0
			self.n_show = 0

	#===PLANT INITIALIZER===
	def __init__(self, name : str, height : float, age : int, growth : float):
		self._name = name
		if height < 0:
			print(f"{self._name}: Error, height can't be negative, is initialized to 0")
			self._height = 0
		else:
			self._height = height
		if age < 0:
			print(f"{self._name}: Error, age can't be negative, is initialized to 0")
			self._age = 0
		else:
			self._age = age
		if growth < 0:
			print(f"{self._name}: Error, factor growthing can't be negative, is initialized to 0.1")
			self._growth = 0.1
		else:
			self._growth = growth
		self._stats = self.Statistic()

	#===PLANT SETTERS===
	def set_height(self, new_value: float) -> None:
		if new_value < 0:
			print(f"{self._name}: Error, height can't be negative")
		else:
			self._height = new_value
			print(f"Height updated: {new_value}cm")

	def set_age(self, new_value: int) -> None:
		if new_value < 0:
			print(f"{self._name}: Error, age can't be negative")
		else:
			self._age = new_value
			print(f"Age updated: {new_value} days old")

	#===PLANT GETTERS===
	def get_name(self) -> str:
		return self._name

	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age

	#===PLANT PRINTER===
	def show(self) -> None:
		self._stats.n_show += 1
		print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

	#===PLANT METHODS===
	def ageing(self) -> None:
		self._stats.n_age += 1
		self._age += 1

	def growing(self) -> None:
		self._stats.n_grow += 1
		self._height += self._growth

	@staticmethod
	def is_older_than_year(age: int) -> bool:
		return age > 365

	@classmethod
	def anonymous(cls) -> "Plant":
		return cls("Unkown", 0.0, 0, 0.0)

	def display_stats(self) -> None:
		print(f"Stats: {self._stats.n_grow} grow, {self._stats.n_age} age, {self._stats.n_show} show")

#=== FLOWER CLASS ===
class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, growth : float, color: str) -> None:
		super().__init__(name, height, age, growth)
		self._color = color
		self._bloomed = False

	#===FLOWER GETTERS===
	def get_color(self) -> str:
		return self._color

	#===PLANT METHODS===
	def blooming(self) -> None:
		self._bloomed = True

	def is_bloomed(self) -> None:
		self.show()

	def show(self) -> None:
		super().show()
		print(f" Color: {self._color}")
		if (self._bloomed == True):
			print(f" {super().get_name()} is blooming beautifully!")
		else:
			print(f" {super().get_name()} has not bloomed yet")

#=== TREE CLASS ===
class Tree(Plant):
	class Statistic(Plant.Statistic):
		def __init__(self):
			super().__init__()
			self.n_shade = 0

	def __init__(self, name: str, height: float, age: int, growth : float,trunk_diameter: float) -> None:
		super().__init__(name, height, age, growth)
		if trunk_diameter > 0:
			self._trunk_diameter = trunk_diameter
		else:
			print(f"{self._diameter}: Error, trunk diameter can't be negative, is initialized to 1")
			self._trunk_diameter = 1

	#===TREE GETTERS===
	def get_trunk_diameter(self) -> float:
		return self._trunk_diameter
	
    #===TREE SETTERS===
	def produce_shade(self) -> None:
		print(f"Tree {super().get_name()} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide.")
		self._stats.n_shade += 1

	def show(self) -> None:
		super().show()
		print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

	def display_stats(self) -> None:
		super().display_stats()
		print(f"{self._stats.n_shade} shade")

class Seed(Flower):
	def __init__(self, name: str, height: float, age: int, growth : float, color: str) -> None:
		super().__init__(name, height, age, growth, color)
		self._seeds = 0

    #===SEED GETTERS===
	def get_seed(self) -> int:
		return self._seeds

	def blooming(self) -> None:
		super().blooming()
		self._seeds = 42

def display_plant_stats(plant: Plant) -> None:
	plant.display_stats()

def main():
    # Flower
	print("==== Garden Analytics ====")
	print("========= Flower =========")
	rose = Flower("Rose", 15.0, 10, 0.8, "red")
	rose.show()
	print()
	print(f"Is the {rose.get_name()} more than a year old? -> {Plant.is_older_than_year(rose.get_age())}")
	print()
	print(f"{rose.get_name()} is blooming.")
	rose.blooming()
	rose.show()
	print()
	print(f"Statistic of {rose.get_name()}")
	display_plant_stats(rose)
	print()

	# Seed
	print("========== Seed ==========")
	sunflower = Seed("Sunflower", 80.0, 45, 0.8, "yellow")
	sunflower.show()
	print()
	print(f"Is the {sunflower.get_name()} more than a year old? -> {Plant.is_older_than_year(sunflower.get_age())}")
	print()
	print(f"{sunflower.get_name()} is growing")
	sunflower.growing()
	print(f"{sunflower.get_name()} is ageing")
	sunflower.ageing()
	print(f"{sunflower.get_name()} is blooming")
	sunflower.blooming()
	sunflower.show()
	print()
	print(f"Statistic of {sunflower.get_name()}")
	display_plant_stats(sunflower)

	# Tree
	print("========== Tree ==========")
	oak = Tree("Oak", 200.0, 366, 2.1, 5.0)
	oak.show()
	print()
	print(f"Is the {oak.get_name()} more than a year old? -> {Plant.is_older_than_year(oak.get_age())}")
	print()
	oak.produce_shade()
	print()
	print(f"Statistic of {oak.get_name()}")
	display_plant_stats(oak)

    # Anonymous plant
	print("======= Anonymous ========")
	anonymous = Plant.anonymous()
	anonymous.show()
	print()
	print(f"Statistic of {oak.get_name()}")
	display_plant_stats(anonymous)



if __name__ == "__main__":
    main()
