# Zadanie polindrom

def czy_polindrom(word):
    Indeks_and_letter = list(enumerate(word))

    def indeks_1(Indeks_and_letter):
        return Indeks_and_letter[0]

    sorted_word = sorted(Indeks_and_letter, key=indeks_1,reverse=True)

    now_word=""
    for _, letter in sorted_word:
        now_word += letter

    polidrom =  now_word == word

    if polidrom:
        print(f'Słowo: "{word}" to palindrom!')
    else:
        print(f'Słowo: "{word}" nie jest palindromem.')

czy_polindrom('anna') # Tu wpisz słowo, aby sprawdzić czy to polindrom.