import random as ra
from unittest import case


input("Pessione Enter")
numero_aleatoio = ra.randrange(0, 25)

print(numero_aleatoio)


match case:

    case 1:
        numero_aleatoio <= 5
        print("You Win!")

    case _:
        print("Tente de novo")
