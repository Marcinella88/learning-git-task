# Zadanie 1 moduł 3

Lista_zakupow = {
        "piekarnia": ["chleb", "bułka", "pączek"],
        "warzywniak":["marchew","seler","rukola"]}

ilosc_produktow = 0

print("Lista zakupów")
for sklepy in Lista_zakupow:
    print(f"Idę do {sklepy.capitalize()} kupuję tu następujące rzeczy: {[produkty.capitalize() for produkty in Lista_zakupow[sklepy]]}") 
    ilosc_produktow += len(Lista_zakupow[sklepy])
print(f"W sumie kupuję {ilosc_produktow} produktów")

print("Zmiana przez drugiego programistę")

print("Branch: kolega_1 chciałbym dopisać tego printa")