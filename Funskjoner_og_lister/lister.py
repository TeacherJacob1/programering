planet0 = "Venus"
planet1 = "Merkur"
planet2 = "Jorden"
planet3 = "Mars"
planet4 = "Jupiter"
planet5 = "Saturn"
planet6 = "Uranus"
planet7 = "Neptun"

solsytem = [planet0,planet1,planet2,planet3,planet4,planet5,planet6,planet7]

print(solsytem)

nyPlanet = "Pluto"
solsytem.append(nyPlanet)

print(solsytem)

solsytem.insert(1, "Aries")

print(solsytem)

solsytem.remove("Pluto")

print(solsytem)

fjernetPlanet = solsytem.pop(1)

print(solsytem)

print(fjernetPlanet)

antPlaneter = 0

for object in solsytem:
    antPlaneter+=1

print(len(solsytem))


solsytem[2] = "Terra"
print(solsytem)

tall = (3,10, 19)

for tallVerdi in tall:
    print(tallVerdi*2)

for index, planet in enumerate(solsytem):
    print(index, planet)


mars = {
    "navn": "Mars",
    "antMaaner" : 2,
    "harRinger" : False
}

print(mars["antMaaner"])
print(mars["harRinger"])