def calculator(number_one, number_two, operator):
    if operator == 1:
        x = number_one + number_two
        print(f"Dodaję {number_one} i {number_two} \nWynik to {x}")
    elif operator == 2:
        x = number_one - number_two
        print(f"Odejmuję {number_one} i {number_two} \nWynik to {x}")
    elif operator == 3: 
        x = number_one * number_two
        print(f"Mnożę {number_one} i {number_two} \nWynik to {x}")
    elif operator == 4:
        x = number_one / number_two
        print(f"Dzielę {number_one} i {number_two} \nWynik to {x}")
    else:
        print("Operator musi być cyfrą od 1-4")
        return

#calculator(4,2,3)

if __name__ == "__main__":
    operator = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    number_one = float(input("Podaj składnik 1."))
    number_two = float(input("Podaj składnik 2."))
    calculator(number_one, number_two, operator)