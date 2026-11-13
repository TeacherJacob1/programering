# 1. Lese drivstoff fra fil
# 2. Vurdere hvor mye drivstoff vi har

fil = open("drivstoff.txt", "r")
drivstoff = int(fil.read())
fil.close()

print("Drivstoff:", drivstoff, "%")


if drivstoff >= 50:
    print("Nok drivstoff")
else:
    print("For lite drivstoff!!!")
