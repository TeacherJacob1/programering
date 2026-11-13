def vis_planet(planet,antall_maaner):
    print("--------------")
    print("Velkommen til " + planet)
    print("Antall måner: " , antall_maaner)
    print("--------------")

vis_planet("Mars", 8)
vis_planet("Saturn", 104)
vis_planet("Terra", 1)

def beregn_avstand(fart, timer):
    avstand = fart * timer
    return 67

resultat = beregn_avstand(4243,334)
print(resultat)

def vurder_temperatur(temperatur):
    if temperatur < -100:
        return "Ekstremt kaldt"
    elif temperatur < 0:
        return "Kaldt"
    elif temperatur < 30:
        return "varmt og godt"
    else:
        return "Jævelig varmt"


print(vurder_temperatur(100))
print(vurder_temperatur(10))
print(vurder_temperatur(50))
print(vurder_temperatur(-103))

#En funskjon som regner ut hvor mye drivstoff et romskip bruker
def drivstoffkalkulator_romskip(time, forbruk_per_time):
    return time * forbruk_per_time

print(drivstoffkalkulator_romskip(1000,6769))