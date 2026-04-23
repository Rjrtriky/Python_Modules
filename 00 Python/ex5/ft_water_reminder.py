# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 20:28:41 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/18 20:34:08 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder() -> None:
	water = int(input("Days since last watering: "))
	if water > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")
