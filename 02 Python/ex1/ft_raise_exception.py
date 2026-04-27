# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rjuarez- <rjuarez-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/27 20:59:22 by rjuarez-          #+#    #+#              #
#    Updated: 2026/04/28 00:27:47 by rjuarez-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str) -> int:
	temp = int(temp_str)
	try:
		temp = int(temp_str)
	except ValueError as e:
		raise ValueError(f"invalid literal for int() with base 10: '{temp_str}'") from e
	if temp < 0:
		raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
	elif temp > 40:
		raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
	return temp

def test_temperature() -> None:
	print("=== Garden Temperature Checker ===\n")
	test_1 = "25"
	print(f"Input data is '{test_1}'")
	try:
		temp = input_temperature(test_1)
		print(f"Temperature is now {temp}°C")
	except ValueError as e:
		print(f"Caught input_temperature error: {e}")
	print()
	test_2 ="abc"
	print(f"Input data is '{test_2}'")
	try:
		temp = input_temperature(test_2)
		print(f"Temperature is now {temp}°C")
	except ValueError as e:
		print(f"Caught input_temperature error: {e}")
	print()
	test_3 = "100"
	print(f"Input data is '{test_3}'")
	try:
		temp = input_temperature(test_3)
		print(f"Temperature is now {temp}°C")
	except ValueError as e:
		print(f"Caught input_temperature error: {e}")
	print()
	test_4 = "-50"
	print(f"Input data is '{test_4}'")
	try:
		temp = input_temperature(test_4)
		print(f"Temperature is now {temp}°C")
	except ValueError as e:
		print(f"Caught input_temperature error: {e}")
	print()
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
	test_temperature()