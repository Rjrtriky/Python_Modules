# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 20:46:53 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/18 20:53:18 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
	days = int(input("Days until harvest: "))
	for i in range(days):
		print("Day ", i + 1)
	print("Harvest time!")
