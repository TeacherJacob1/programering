from random import randint, choice
from math import sqrt




planetNummer = randint(0,99999)

print(planetNummer)


planeter = [
    "Merkur",
    "Venus",
    "Jorden",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]

print(choice(planeter))

print(sqrt(randint(0,16)))