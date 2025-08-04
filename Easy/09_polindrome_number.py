def is_polindrome(num):
	if num < 0:
		return False

	original_num = num
	reversed_num = 0

	while num > 0:
		reversed_num = reversed_num * 10 + num % 10
		num //= 10
	
	return reversed_num == original_num

if __name__ == '__main__':
	numbers = [121, -121, 10, 131, 333, 324]
	for num in numbers:
		print(is_polindrome(num))