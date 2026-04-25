# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/24 19:15:36 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/26 00:14:31 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#=== PLANT CLASS ===
class Plant:
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
		print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

	#===PLANT METHODS===
	def ageing(self) -> None:
		self._age += 1

	def growing(self) -> None:
		self._height += self._growth

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
		print(f"{self._name} is blooming beautifully!")

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
	def __init__(self, name: str, height: float, age: int, growth : float,trunk_diameter: float, produce_shade: bool) -> None:
		super().__init__(name, height, age, growth)
		if trunk_diameter > 0:
			self._trunk_diameter = trunk_diameter
		else:
			print(f"{self._diameter}: Error, trunk diameter can't be negative, is initialized to 1")
			self._trunk_diameter = 1
		self._produce_shade = produce_shade

	#===TREE GETTERS===
	def get_trunk_diameter(self) -> float:
		return self._trunk_diameter
	
    #===TREE SETTERS===
	def set_produce_shade(self, shade: bool) -> None:
		self._produce_shade = shade

	#===TREE METHODS===
	def is_shade(self) -> None:
		if (self._produce_shade):
			print(f"Tree {super().get_name()} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide.")
		else:
			print(f"Tree {super().get_name()} now not produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide.")

	def show(self) -> None:
		super().show()
		print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

#=== VEGETABLE CLASS ===
class Vegetable(Plant):
	def __init__(self, name: str, height: float, age: int, growth : float, harvest_season: str, nutritional_value: int) -> None:
		super().__init__(name, height, age, growth)
		self._harvest_season = harvest_season
		if nutritional_value < 0:
			print(f"{self._name}: Error, nutritional value can't be negative, is initialized to 0")
			self._nutritional_value = 0
		else:
			self._nutritional_value = nutritional_value

	#===VEGETABLE GETTERS===
	def get_harvest_season(self) -> str:
		return self._harvest_season

	def get_nutritional_value(self) -> int:
		return self._nutritional_value

	#===VEGETABLE SETTERS===
	def set_nutritional_value(nutritional_value: int) -> None:
		if nutritional_value < 0:
			print(f"{self._name}: Error, nutritional value can't be negative")
		else:
			self._nutritional_value = nutritional_value

	#===VEGETABLE METHODS===
	def show(self) -> None:
		super().show()
		print(f"Harvest season: {self._harvest_season}")
		print(f"Nutritional value: {self._nutritional_value}")

	def ageing_one(self) -> None:
		super().ageing()
		super().growing()
		self._nutritional_value +=1

def main() -> None:
	print("=== Garden Plant Types ===")
	print("========= Flower =========")
	rose = Flower("Rose", 15.0, 10,0.8 , "red")
	rose.show()
	print()
	print(f"The {rose.get_name()} is blooming:")
	rose.blooming()
	print()
	print(f"Is the {rose.get_name()}  blooming?")
	rose.is_bloomed()
	print()
	print("========== Tree ==========")
	oak = Tree("Oak", 200, 365, 0.5, 5.4, False)
	oak.show()
	print()
	print(f"Does the {oak.get_name()} tree produce shade?")
	oak.is_shade()
	print()
	print("Now it produce shade")
	oak.set_produce_shade(True)
	oak.is_shade()
	print()
	print("======== Vegetable =======")
	tomato = Vegetable("Tomato", 5, 10, 2.3, "April", 0)
	tomato.show()
	print()
	print(f"{tomato.get_name()} grow for 20 days:")
	for i in range(1, 20):
		tomato.ageing_one()
	tomato.show()

if __name__ == "__main__":
    main()
