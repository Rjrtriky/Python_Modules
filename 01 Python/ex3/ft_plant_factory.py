# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/24 16:51:06 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/24 22:04:37 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age, growth):
		self.name = name
		self.height = height
		self.age = age
		self.growth = growth
		print(f"Created: {self.name}: {round(self.height, 1)}cm, {self.age} days old")

	def show(self) -> None:
		print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

	def ageing(self) -> None:
		self.age += 1

	def growing(self) -> None:
		self.height += self.growth

def main () -> None:
	print("=== Plant Factory Output ===")
	rose = Plant("Rose", 25.0, 30, 0.8)
	oak = Plant("Oak", 200.0, 365, 0.6)
	cactus = Plant("Cactus", 5.0, 90, 0.1)
	sunflower = Plant("Sunflower", 80.0, 45, 0.2)
	fern = Plant("Fern", 15.0, 120, 0.1)

if __name__ == "__main__":
	main()