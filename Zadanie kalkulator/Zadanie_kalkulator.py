import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(number_one, number_two, operator):
    if operator == 1:
        x = number_one + number_two
        print(f"Wynik to {x}")
    elif operator == 2:
        x = number_one - number_two
        print(f"Wynik to {x}")
    elif operator == 3: 
        x = number_one * number_two
        print(f"Wynik to {x}")
    elif operator == 4:
        x = number_one / number_two
        print(f"Wynik to {x}")
    else:
        print("Operator musi być cyfrą od 1-4")
        return

if __name__ == "__main__":
    operator = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    description = ("Dodaję1" if operator == 1 else 
                   "Odejmuję" if operator == 2 else 
                   "Mnożę"if operator == 3 else 
                   "Dzielę" if operator == 4 else 
                   "Nic nie robię")
    number_one = float(input("Podaj składnik 1. "))
    number_two = float(input("Podaj składnik 2. "))
    logging.debug(f"{description} {number_one} i {number_two}")
    calculator(number_one, number_two, operator)