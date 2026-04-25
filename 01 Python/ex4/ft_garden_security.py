# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/24 16:51:06 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/25 14:46:10 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

#=== CLASS ===
class Plant:
	#===INITIALIZER===
	def __init__(self, name:str, height:float, age:int, growth:float):
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
		print(f"Plant created: {self._name}: {round(self._height, 1)}cm, {self._age} days old")

	#===SETTERS===
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

	#===GETTERS===
	def get_name(self) -> str:
		return self._name

	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age
	
	def get_growth(self) -> float:
		return self._growth
	
	#===PRINTER===
	def show(self) -> None:
		print(f"Current state: {self._name}: {round(self._height, 1)}cm, {self._age} days old")

	#===METHODS===
	def ageing(self) -> None:
		self._age += 1

	def growing(self) -> None:
		self._height += self._growth

def main () -> None:
	print("=== Garden Security System ===")
	rose = Plant("Rose", 25.0, 30, 0.8)
	print("")
	oak = Plant("Oak", -200.0, -1, -0.8)
	print("")
	print("GETTERS")
	print("=======")
	print(f"Plant name: {rose.get_name()}")
	print(f"Plant height: {rose.get_height()}")
	print(f"Plant age: {rose.get_age()}")
	print(f"Plant growth factor: {rose.get_growth()}")
	print("")
	print("SETTERS")
	print("=======")
	print(f"Change of positive height ({rose.get_height()} to 4.5):")
	rose.set_height(4.5)
	rose.show()
	print("")
	print(f"Change of negative height ({rose.get_height()} to -0.5):")
	rose.set_height(-0.5)
	rose.show()
	print("-------")
	print(f"Change of positive age ({rose.get_age()} to 45):")
	rose.set_age(45)
	rose.show()
	print("")
	print(f"Change of negative age ({rose.get_age()} to -5):")
	rose.set_age(-5)
	rose.show()

if __name__ == "__main__":
	main()