# Caesar cipher

max_key_size = 26

def getMode():
	while True:
		print("Would you like to encrypt, decrypt, or brute force a message?")
		mode = input().lower()
		if mode in 'encrypt e decrypt d brute b'.split():
			return mode
		else:
			print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd' or 'brute' or 'b' to proceed.")

def getMessage():
	print("Enter your message:")
	return input()

def getKey():
	key = 0
	while True:
		print("Enter the key number (0-%s)" % (max_key_size))
		key = int(input())
		if key >= 1 and key <= max_key_size:
			return key

def getTranslatedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num = num + key
			if symbol.isupper():
				if num > ord('Z'):
					num = num - 26
				elif num < ord('A'):
					num = num + 26

			elif symbol.islower():
				if num > ord('z'):
					num = num - 26
				elif num < ord('a'):
					num = num + 26
			translated = translated + chr(num)
		else:
			translated = translated + symbol
	return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
	key = getKey()

print("Your translated text is:")
if mode[0] != 'b':
	print(getTranslatedMessage(mode, message, key))
else:
	for key in range(1, max_key_size + 1):
		print(key, getTranslatedMessage(mode, message, key))
