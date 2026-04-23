# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 20:16:11 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/18 20:25:22 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() -> None:
	age = int(input("Enter plant age in days: "))
	if age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
