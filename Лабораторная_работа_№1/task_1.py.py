numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

kol_numbers = len(numbers)
sum_numbers = sum(numbers[:4]+numbers[5:])
sr_arif_numbers = sum_numbers / kol_numbers

numbers[4] = sr_arif_numbers

print("Измененный список:", numbers)
