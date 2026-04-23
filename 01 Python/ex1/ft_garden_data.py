# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/23 21:29:41 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/23 22:08:42 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age
        def ft_print_plant(self) -> None:
              print(f"{self.name}: {self.height}cm, {self.age} days old")

def main() -> None:
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    
    print("=== Garden Plant Registry ===")
    plant_1.ft_print_plant()
    plant_2.ft_print_plant()
    plant_3.ft_print_plant()

if __name__ == "__main__":
      main()