
while True:
    pyg = 'ay'

    original = input("Enter a word: ")

    if len(original) > 0 and original.isalpha():
        print(original)
        word = original.lower()
        first = word[0]
        new_word = word[1:] + first + pyg
        print("Your translated word in pig latin is \"" + new_word + "\"")

    else:
        print("Your word is empty or it has symbols or numbers that is not recognized. Try again.")
