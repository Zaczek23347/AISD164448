def zad1(txt1, txt2):
    return (txt1 + "." + txt2)


print(zad1("J", "Kowalski"))


def zad2(im, naz):
    im = im.title()
    naz = naz.title()
    return (im[0] + "." + naz)


print(zad2("kacper", "zaczek"))


def zad3(ts, dj, wiek):
    ts = ts * 100
    rok = ts + dj
    return (rok - wiek)


print(zad3(20, 22, 21))


def zad4(im, naz, funkcja):
    return funkcja(im, naz)


print("jan", "kowalski", zad2)


def zad5(x, y):
    if (x < 0 or y < 0):
        return ("jedna z liczb jest ujemna")
    if (y == 0):
        return ("druga liczba nie moze byc rowna 0")
    return (x / y)


print(zad5(10, 2))

# zad6
x = 0
while x <= 100:
    x = x + int(input("x="))
print(x)


#
def zad7(lista):
    krotka = tuple((x for x in lista))
    return krotka


lista = [1, 5, 12, "Adam", "Tomek", "Bartosz", 4]
print(lista)
print((listadokrotki(lista)))

# zad8
lista = []
for i in range(0, 5):
    x = input("X=")
    lista.append(x)
print((listadokrotki(lista)))


def zad9(x):
    return {
        1: 'Poniedziałek',
        2: 'Wtorek',
        3: 'Środa',
        4: 'Czwartek',
        5: 'Piątek',
        6: 'Sobota',
        7: 'Niedziela',
    }.get(x, 'Wprowadź numer od 1 do 7')


print(dzientygodnia(1))
