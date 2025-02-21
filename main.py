# Zadanie: 3.2. Śledzenie zmian w kodzie

Lista_zakupow = {
        "piekarnia": ["chleb", "bułka", "pączek"],
        "warzywniak":["marchew","seler","rukola"]
        }

print("Lista zakupów")
for sklepy in Lista_zakupow:
    print(f"Idę do {sklepy.capitalize()} kupuję tu następujące rzeczy: {[produkty.capitalize() for produkty in Lista_zakupow[sklepy]]}")
