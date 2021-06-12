#Python 3.9 Generator Haseł 2

import random
import string

długość = int(input("Wpisz długość hasła: "))

password = "".join([random.choice(string.ascii_letters) for _ in range (długość)])
print("Wygenerowane hasło (litery duże i małe): ", password)

password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range (długość)])
print("Wygenerowane hasło (małe litery, duże litery, znaki specjalne oraz cyfry): ", password)