import random


input_text = 'Hello my name is Alex and I have just created my first encrypter.'

char_pool = ''

key = ''

temp_encrypted = ''

encrypted = ''

temp_decrypted = ''

e_char = ''

decrypted = ''

for i in range(0x00, 0xFF):
	char_pool += chr(i)

number_of_bytes = 256 // 8

for i in range(number_of_bytes):
	key += random.choice(char_pool)

og_key = key

index = 0

padding_needed = len(input_text) % 12

if padding_needed > 0:
	for i in range(12 - padding_needed):
		input_text += ' '


for i in range(0,9,1):
	for char in input_text:
		if index > (len(key) - 1):
			index = 0
		char = chr(ord(char) ^ ord(key[index]))
		index += 1
		temp_encrypted += char
	key = temp_encrypted
	encrypted = temp_encrypted
	temp_encrypted = ''
	index = 0


index = 0

key = og_key

for i in range(0,9,1):
	for char in encrypted:
		if index > (len(key) - 1):
			index = 0
		key_char = chr(ord(char) ^ ord(key[index]))
		index += 1
		temp_decrypted += key_char
	key = temp_decrypted
	decrypted = temp_decrypted
	temp_decrypted = ''
	index = 0


print(encrypted)

print(decrypted)






def mix():

	number_of_rows = len(decrypted) // 4

	mixing_bowl = {}

	index = 0

	for i in range(number_of_rows):
		mixing_bowl[i] = [input_text[0 + index], input_text[1 + index], input_text[2 + index], input_text[3 + index]]

		# , input_text[4 + index], input_text[5 + index], input_text[6 + index], input_text[7 + index], input_text[8 + index]]
		index += 4


	index = 0

	mixed_input = ''

	for i in range(len(mixing_bowl)):	

		if index > len(mixing_bowl):
			break

		# mixed_input += mixing_bowl[index][0] + mixing_bowl[index][1] + mixing_bowl[index][2] + mixing_bowl[index][3]

		if index + 1 >= len(mixing_bowl):
			break
		mixing_bowl[index + 1] = [mixing_bowl[index+1][1], mixing_bowl[index+1][2], mixing_bowl[index+1][3], mixing_bowl[index+1][0]]

		# mixed_input += mixing_bowl[index+1][1] + mixing_bowl[index+1][2] + mixing_bowl[index+1][3] + mixing_bowl[index+1][0]

		if index + 2 >= len(mixing_bowl):
			break
		mixing_bowl[index + 2] = [mixing_bowl[index+2][2], mixing_bowl[index+2][3], mixing_bowl[index+2][0], mixing_bowl[index+2][1]]

		# mixed_input += mixing_bowl[index+2][2] + mixing_bowl[index+2][3] + mixing_bowl[index+2][0] + mixing_bowl[index+2][1]

		if index + 3 >= len(mixing_bowl):
			break
		mixing_bowl[index + 3] = [mixing_bowl[index+3][3], mixing_bowl[index+3][0], mixing_bowl[index+3][1], mixing_bowl[index+3][2]]

		# mixed_input += mixing_bowl[index+3][3] + mixing_bowl[index+3][0] + mixing_bowl[index+3][1] + mixing_bowl[index+3][2]

		index += 4


	for i in range(len(mixing_bowl)):	
		mixed_input += mixing_bowl[i][2] + mixing_bowl[i][3] + mixing_bowl[i][0] + mixing_bowl[i][1]





def reverse_mix():


	fixed_input = ''


	number_of_rows = len(decrypted) // 4

	fixing_bowl = {}

	index = 0

	for i in range(number_of_rows):
		fixing_bowl[i] = [mixed_input[0 + index], mixed_input[1 + index], mixed_input[2 + index], mixed_input[3 + index]]

		# , input_text[4 + index], input_text[5 + index], input_text[6 + index], input_text[7 + index], input_text[8 + index]]
		index += 4


	for i in range(len(fixing_bowl)):	
		fixed_input += fixing_bowl[i][2] + fixing_bowl[i][3] + fixing_bowl[i][0] + fixing_bowl[i][1]



	fixing_bowl = {}

	index = 0

	for i in range(number_of_rows):
		fixing_bowl[i] = [fixed_input[0 + index], fixed_input[1 + index], fixed_input[2 + index], fixed_input[3 + index]]

		# , input_text[4 + index], input_text[5 + index], input_text[6 + index], input_text[7 + index], input_text[8 + index]]
		index += 4

	index = 0

	print(fixing_bowl)


	fixed_input = ''


	for i in range(len(fixing_bowl)):	

		if index > len(fixing_bowl):
			break

		fixed_input += fixing_bowl[index][0] + fixing_bowl[index][1] + fixing_bowl[index][2] + fixing_bowl[index][3]

		if index + 1 >= len(fixing_bowl):
			break
		fixing_bowl[index + 1] = [fixing_bowl[index+1][3], fixing_bowl[index+1][0], fixing_bowl[index+1][1], fixing_bowl[index+1][2]]

		fixed_input += fixing_bowl[index+1][0] + fixing_bowl[index+1][1] + fixing_bowl[index+1][2] + fixing_bowl[index+1][3]

		if index + 2 >= len(fixing_bowl):
			break
		fixing_bowl[index + 2] = [fixing_bowl[index+2][2], fixing_bowl[index+2][3], fixing_bowl[index+2][0], fixing_bowl[index+2][1]]

		fixed_input += fixing_bowl[index+2][0] + fixing_bowl[index+2][1] + fixing_bowl[index+2][2] + fixing_bowl[index+2][3]

		if index + 3 >= len(fixing_bowl):
			break
		fixing_bowl[index + 3] = [fixing_bowl[index+3][1], fixing_bowl[index+3][2], fixing_bowl[index+3][3], fixing_bowl[index+3][0]]

		fixed_input += fixing_bowl[index+3][0] + fixing_bowl[index+3][1] + fixing_bowl[index+3][2] + fixing_bowl[index+3][3]

		index += 4

	fixed_input = fixed_input.rstrip()
		

	print(fixed_input)