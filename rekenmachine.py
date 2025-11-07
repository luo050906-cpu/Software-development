print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y?")
print("[2] Hoeveel % is x van y?")
print("[3] x neemt toe met y%; hoeveel heb je nu?")
print("[4] x neemt af met y%; hoeveel heb je nu?")
print("[5] Van oud naar nieuw: met hoeveel % toegenomen?")
print("[6] Van oud naar nieuw: met hoeveel % afgenomen?")

choice = input("Welke optie kies je? ")

match choice:
    case "1":
        x = float(input("Wat is x? "))
        y = float(input("Wat is y? "))
        answer = x / 100 * y
        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "% = " + str(x/100) + " en " + str(x/100) + " x " + str(y) + " = " + str(answer))

    case "2":
        x = float(input("Wat is x? "))
        y = float(input("Wat is y? "))
        answer = x / y * 100
        print("De vraag is: hoeveel % is " + str(x) + " van " + str(y) + "?")
        print("Het antwoord is: " + str(answer) + "%")
        print("De berekening is: " + str(x) + " : " + str(y) + " = " + str(x/y) + " en " + str(x/y) + " x 100 = " + str(answer) + "%")

    case "3":
        x = float(input("Wat is het begingetal (x)? "))
        y = float(input("Met hoeveel procent neemt het toe (y)? "))
        answer = x * (1 + y / 100)
        print("De vraag is: " + str(x) + " neemt toe met " + str(y) + "%.")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + " x (1 + " + str(y) + "/100) = " + str(answer))

    case "4":
        x = float(input("Wat is het begingetal (x)? "))
        y = float(input("Met hoeveel procent neemt het af (y)? "))
        answer = x * (1 - y / 100)
        print("De vraag is: " + str(x) + " neemt af met " + str(y) + "%.")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + " x (1 - " + str(y) + "/100) = " + str(answer))

    case "5":
        oud = float(input("Wat is het oude bedrag? "))
        nieuw = float(input("Wat is het nieuwe bedrag? "))
        answer = (nieuw / oud - 1) * 100
        print("De vraag is: van " + str(oud) + " naar " + str(nieuw) + ", met hoeveel procent toegenomen?")
        print("Het antwoord is: " + str(answer) + "%")
        print("De berekening is: (" + str(nieuw) + " / " + str(oud) + " - 1) x 100 = " + str(answer) + "%")

    case "6":
        oud = float(input("Wat is het oude bedrag? "))
        nieuw = float(input("Wat is het nieuwe bedrag? "))
        answer = (1 - nieuw / oud) * 100
        print("De vraag is: van " + str(oud) + " naar " + str(nieuw) + ", met hoeveel procent afgenomen?")
        print("Het antwoord is: " + str(answer) + "%")
        print("De berekening is: (1 - " + str(nieuw) + " / " + str(oud) + ") x 100 = " + str(answer) + "%")

    case _:
        print("Je hebt een ongeldige optie gekozen.")
