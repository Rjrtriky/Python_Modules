# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 22:47:59 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/20 21:11:42 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	prefix = f"{seed_type.capitalize()} seeds:"
	if unit == "packets":
		print(f"{prefix} {quantity} packets available")
	elif unit == "grams":
		print(f"{prefix} {quantity} grams total")
	elif unit == "area":
		print(f"{prefix} covers {quantity} square meters")
	else:
		print("Unknown unit type")
