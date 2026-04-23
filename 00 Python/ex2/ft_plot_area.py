# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/18 19:50:31 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/18 20:00:32 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	print("Plot area: ", length * width)
