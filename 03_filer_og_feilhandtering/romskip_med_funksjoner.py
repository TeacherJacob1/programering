def vurder_drivstoff(prosent):
    if prosent >= 50:
        return "Nok drivstoff"
    else:
        return "For lite drivstoff"


def les_drivstoff():
    fil = open("drivstoff.txt", "r")
    drivstoff = int(fil.read())
    fil.close()
    return drivstoff


print("Drivstoff:", les_drivstoff(), "%")
print(vurder_drivstoff(les_drivstoff()))

