# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 20:57:41 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/27 22:28:25 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str) -> int:
	return int(temp_str)

def test_temperature() -> None:
	print("=== Garden Temperature ===")
	valid = "25"
	print(f"Input data is '{valid}'")	
	try:
		temp = input_temperature(valid)
		print(f"Temperature is now {temp}°C")
	except Exception as e:
		print(f"Caught input_temperature error: {e}")
	print()
	invalid = "abc"
	print(f"Input data is '{invalid}'")
	try:
		temp = input_temperature(invalid)
		print(f"Temperature is now {temp}°C")
	except Exception as e:
		print(f"Caught input_temperature error: {e}")
	print()
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
	test_temperature()