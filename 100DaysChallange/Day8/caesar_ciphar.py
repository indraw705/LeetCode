from art import logo

should_continue = True
while should_continue:
    alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    print(logo)
    direction = input("Type 'encode' for Encode message \nType 'decode' for Decode message: \n")
    text = input("Type your Message here:\n")
    shift = int(input("Type your Shift Number:\n"))


    def caesar(start_text, shift_amount, direction):
        new_text = ""
        shift_amount = shift_amount % 26
        if direction == 'decode':
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                new_text += new_letter
            else:
                new_text += letter
        print(f"the {direction}d text is {new_text}")


    caesar(text, shift, direction)
    print("+++"*15+"-"*5+"+++"*15)
    should_continue = input("do you want to continue ???\n")
    if should_continue == "yes":
        should_continue = True
    else:
        should_continue = False
        print("Good Bye")

