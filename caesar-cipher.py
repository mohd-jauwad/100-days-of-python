alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run = True
while run:
  print()
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def encrypt(plain_text, shift_amount):
    plain_text = list(text)
    cipher_text = []
    for i in range(0, len(plain_text)):
      cipher_text += alphabet[(alphabet.index(plain_text[i])+ shift) % 26]
    print(cipher_text) 

  def decrypt(plain_text, shift_amount):
    cipher_text = list(text)
    plain_text = ""
    for i in range(0, len(cipher_text)):
      plain_text += alphabet[(alphabet.index(cipher_text[i])- shift) % 26]
    print(f"The decrypted text is : {plain_text}\n") 

  if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
  elif direction == "decode":
    decrypt(plain_text=text,shift_amount=shift)

  proceed = input("Would you like to continue? y or n ")
  if proceed == "y":
    run == True
  if proceed == "n":
    print("Thank you. Good bye.")
    run == False