#fil = open("filOperasjoner/planeter.txt","a")
#fil.write("Mars\n")
#fil.close

#with open("filOperasjoner/planeter.txt","r") as fil:
 #   for linje in fil:
  #      print(linje.strip())

planet = input("Skriv inn en planet: ")
antMaaner = input("Antall måner: ")

with open("filOperasjoner/planeter.txt","w") as fil:
    fil.write(planet + "\n")
    fil.write(antMaaner)

with open("filOperasjoner/planeter.txt","r") as fil:
    print(fil.read())

print("Planeten ble lagret")

with open("galaxe.txt", "r") as fil:
    print(fil.read())