# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 22:02:38 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/18 22:43:14 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_day(day) -> None:
	if day > 0:
		ft_count_day(day - 1)
		print("Day ", day)

def ft_count_harvest_recursive() -> None:
	days = int(input("Days until harvest: "))
	ft_count_day(days)
	print("Harvest time!")
