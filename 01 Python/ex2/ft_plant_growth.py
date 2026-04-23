# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/23 22:09:35 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/23 23:47:10 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age, growth):
		self.name = name
		self.height = height
		self.age = age
		self.growth = growth

	def print_plant(self) -> None:
		print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

	def ageing(self) -> None:
		self.age += 1

	def growing(self) -> None:
		self.height += self.growth

def main() -> None:
	rose = Plant("Rose", 25.0, 30, 0.8)
	size = rose.height
	
	print("===== Garden Plant Growth ====")
	rose.print_plant()
	for day in range(1, 8):
		rose.ageing()
		rose.growing()
		print(f"=== Day {day} ===")
		rose.print_plant()
	
	size = rose.height - size
	print(f"Growth this week: {round(size,1)}cm")

if __name__ == "__main__":
	main()
