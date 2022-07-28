import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_collection = []

password_collection.append(random.choices(letters, k=nr_letters))
password_collection.append(random.choices(numbers, k=nr_numbers))
password_collection.append(random.choices(symbols, k=nr_symbols))

#print(password_collection)

#next step, remove nested lists and allocate all elements from lists into a single list

#[[a], [b], [c]]

flat_list = []

for lists in password_collection:
    if type(lists) is list:
        for items in lists:
            flat_list.append(items)
    else:
        flat_list.append(lists)

random.shuffle(flat_list)

print(''.join(flat_list))

