'''
Programa minibiužetas 1. Programa duomenis(skaičius) apie pajamas ir išlaidas saugos dviejuose listuose - pajamos ir islaidos,
turės pasirinkimų meniu -
1. įvesti pajamas,
2. įvesti išlaidas,
q išeiti(vartotojas valdys įvesdamas skaičius)
ir dar vieną pasirinkimą, kurį pridėsim vėliau.
* Sukuriame meniu su vartotojo pasirinkimais, kurie kartojami, kol vartotojas nepaspaudžia - q(išeiti)
* Sukuriame pajamų įvedimo funkcionalumą.
Pasirinkus 1 programa leidžia vartotojui įvesti pajamas ir
prijungia prie pajamų listo(testuodami vis atsispausdinam pajamų listą, kad matytume jog jis pildosi).
* Analogiškai sukuriam išlaidų įvedimo funkcionalumą.
* Sukuriam naują meniu punktą - 3. rodyti ataskaitą,
jį pasirinkus programa turi atspausdinti pajamų listą ir išlaidų listą.
* Patobulinam ataskaitą, programa turi atspausdinti pajamų sumą, išlaidų sumą ir balansą(pajamos - išlaidos).
'''
pajamos = []
islaidos = []

while True:
    opcija = input("Pasirinkite opcija:\n(1) Ivesti pajamas\n(2) Ivesti islaidas\n(3) Rodyti ataskaita\n(q) Iseiti\n|  ").lower()
    if opcija == "1":
        skaicius = round(float(input("Pajamos: ")), 2)
        pajamos.append(skaicius)
        print(pajamos)
    elif opcija == "2":
        skaicius = round(float(input("ISlaidos: ")), 2)
        islaidos.append(skaicius)
        print(islaidos)
    elif opcija == "3":
        print(f"Pajamos: {pajamos}\nIslaidos: {islaidos}")
        pajamu_suma = sum(pajamos)
        islaidu_suma = sum(islaidos)
        balansas = (pajamu_suma - islaidu_suma)
        print(f"Viso pajamu: {pajamu_suma}\nViso islaidu: {islaidu_suma}\nBalansas: {balansas}")

    elif opcija == "q":
        break
    else:
        print("Tokios opcijos nera")
        continue
