import random










def create_key():

	char_pool = ''

	key = ''

	for i in range(0x00, 0xFF):
		char_pool += chr(i)

	number_of_bytes = 256 // 8

	for i in range(number_of_bytes):
		key += random.choice(char_pool)

	return key











def encrypt(message, key):
	temp_encrypted = ''

	encrypted = ''

	og_key = key

	index = 0

	padding_needed = len(message) % 12

	if padding_needed > 0:
		for i in range(12 - padding_needed):
			message += ' '


	for i in range(0,9,1):
		for char in message:
			if index > (len(key) - 1):
				index = 0
			char = chr(ord(char) ^ ord(key[index]))
			index += 1
			temp_encrypted += char

		temp_encrypted = mix(temp_encrypted)

		key = temp_encrypted
		encrypted = temp_encrypted
		temp_encrypted = ''
		index = 0
	
	return encrypted











def decrypt(encrypted, key):

	temp_decrypted = ''

	decrypted = ''

	index = 0

	demixed_encrypted = ''
	encrypted = reverse_mix(encrypted)

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

	return decrypted.rstrip()








def mix(encrypted):

	number_of_rows = len(encrypted) // 4

	mixing_bowl = {}

	index = 0

	for i in range(number_of_rows):
		mixing_bowl[i] = [encrypted[0 + index], encrypted[1 + index], encrypted[2 + index], encrypted[3 + index]]
		index += 4

	index = 0

	mixed_input = ''

	index_length = len(mixing_bowl) - 1

	for i in range(len(mixing_bowl)):	

		if index > index_length:
			break

		if index + 1 > index_length:
			break
		mixing_bowl[index + 1] = [mixing_bowl[index+1][1], mixing_bowl[index+1][2], mixing_bowl[index+1][3], mixing_bowl[index+1][0]]

		if index + 2 > index_length:
			break
		mixing_bowl[index + 2] = [mixing_bowl[index+2][2], mixing_bowl[index+2][3], mixing_bowl[index+2][0], mixing_bowl[index+2][1]]

		if index + 3 > index_length:
			break
		mixing_bowl[index + 3] = [mixing_bowl[index+3][3], mixing_bowl[index+3][0], mixing_bowl[index+3][1], mixing_bowl[index+3][2]]

		index += 4


	for i in range(len(mixing_bowl)):	
		mixed_input += mixing_bowl[i][2] + mixing_bowl[i][3] + mixing_bowl[i][0] + mixing_bowl[i][1]


	return mixed_input



def reverse_mix(decrypted):


	fixed_input = ''


	number_of_rows = len(decrypted) // 4

	fixing_bowl = {}

	index = 0

	for i in range(number_of_rows):
		fixing_bowl[i] = [decrypted[0 + index], decrypted[1 + index], decrypted[2 + index], decrypted[3 + index]]

		# , input_text[4 + index], input_text[5 + index], input_text[6 + index], input_text[7 + index], input_text[8 + index]]
		index += 4


	for i in range(len(fixing_bowl)):	
		fixed_input += fixing_bowl[i][2] + fixing_bowl[i][3] + fixing_bowl[i][0] + fixing_bowl[i][1]


	fixing_bowl = {}

	index = 0

	for i in range(number_of_rows):
		fixing_bowl[i] = [fixed_input[0 + index], fixed_input[1 + index], fixed_input[2 + index], fixed_input[3 + index]]
		index += 4

	index = 0


	fixed_input = ''

	index_length = len(fixing_bowl) - 1;

	for i in range(len(fixing_bowl)):	

		if index >= index_length:
			break

		fixed_input += fixing_bowl[index][0] + fixing_bowl[index][1] + fixing_bowl[index][2] + fixing_bowl[index][3]

		if index + 1 > index_length:
			break
		fixing_bowl[index + 1] = [fixing_bowl[index+1][3], fixing_bowl[index+1][0], fixing_bowl[index+1][1], fixing_bowl[index+1][2]]

		fixed_input += fixing_bowl[index+1][0] + fixing_bowl[index+1][1] + fixing_bowl[index+1][2] + fixing_bowl[index+1][3]

		if index + 2 > index_length:
			break
		fixing_bowl[index + 2] = [fixing_bowl[index+2][2], fixing_bowl[index+2][3], fixing_bowl[index+2][0], fixing_bowl[index+2][1]]

		fixed_input += fixing_bowl[index+2][0] + fixing_bowl[index+2][1] + fixing_bowl[index+2][2] + fixing_bowl[index+2][3]

		if index + 3 > index_length:
			break
		fixing_bowl[index + 3] = [fixing_bowl[index+3][1], fixing_bowl[index+3][2], fixing_bowl[index+3][3], fixing_bowl[index+3][0]]

		fixed_input += fixing_bowl[index+3][0] + fixing_bowl[index+3][1] + fixing_bowl[index+3][2] + fixing_bowl[index+3][3]

		index += 4

	fixed_input = fixed_input.rstrip()
		
	return fixed_input








input_text = 'WOO! TEST STRING BABY IN AND OUT LET\'S GO!!!!'


key = create_key()

og_key = key

encrypted = encrypt(input_text, key)

decrypted = decrypt(encrypted, key)


print('Input :' + input_text + '\n')

print('Encrypted: ' + encrypted + '\n')

print('Decrypted: ' + decrypted)
