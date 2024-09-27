import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("""
                     
                                             
                  █████████                  
                █████▒░▒█████                
               ███▒       ▒███               
              ███▒         ░███              
              ███           ███              
              ███           ███              
             ███████████████████             
            █████████████████████            
            █████████████████████            
            ████████     ████████            
            ████████     ████████            
            █████████   █████████            
            █████████   █████████            
            █████████   █████████            
            █████████████████████            
            ▒███████████████████▓            
                                             
                                                                                                                                                                                                                                                                                                                                                                                                                
 """)
print("Welcome to the Python Password Generator!")
print("")
nr_letters = int(input("How many letters would you like in your password?\n"))
print("")
nr_symbols = int(input(f"How many symbols would you like?\n"))
print("")
nr_numbers = int(input(f"How many numbers would you like?\n"))
print("")

# OPTION 1 Easy level (The position of the characters won't be random)

# password = ""

# # letters
# for character in range(1, nr_letters + 1):
#     # 1 - 4
#     random_character = random.choice(letters)
#     password = password + random_character

# # symbols
# for character in range(1, nr_symbols + 1):
#     random_character = random.choice(symbols)
#     password = password + random_character

# # numbers
# for character in range(1, nr_numbers + 1):
#     random_character = random.choice(numbers)
#     password = password + random_character

# print(password)


#/////////////////////////////////////////////////////////////////////////


# OPTION 2 Hard level (The position of the characters is random)

password_list = []

# letters
for character in range(0, nr_letters):
    password_list.append(random.choice(letters))

# symbols
for character in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# numbers
for character in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)
# Esto es para poner la posicion de los characters de manera aleatoria, es decir, que los numbers o symbols no esten siempre en el mismo index o posicion

# e.g sin shuffle (letras, numeros y simbolos estan en el mismo index:
    # ['p', 'E', 'V', '*', '&', '!', '1', '5', '1']
    # ['X', 'J', 'n', '$', '+', '%', '3', '7', '7']

random.shuffle(password_list)
# e.g con shuffle (aqui si las letras, numeros y simbolos cambian de forma random su index)
    # ['3', 'J', '%', 'n', '+', '$', 'X', '7', '7']
    # ['l', '(', '&', 's', 'B', '0', '8', ')', '5']
# print(password_list)

# Aqui ponemos el password dentro de una string
password = ""
for character in password_list:
    password += character    
# Here we print the final output:    
print(f"Perfect, here is your password:\n{password}")
print("")


