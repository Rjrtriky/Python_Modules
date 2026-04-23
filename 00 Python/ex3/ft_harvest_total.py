# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 20:05:44 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/18 20:13:17 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
	total = 0
	harvest = int(input("Day 1 harvest: "))
	total = harvest
	harvest = int(input("Day 2 harvest: "))
	total = total + harvest
	harvest = int(input("Day 3 harvest: "))
	total = total + harvest
	print("Total harvest: ", total)
