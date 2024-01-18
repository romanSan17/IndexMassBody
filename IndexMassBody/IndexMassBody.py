print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis on sinu nimi?")
print(nimi, ", oi kui ilus nimi!")
yesno=int(input("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if mass==1:
    koddus=int(input("milline kõrgus?"))
    mass=int(input("milline kaal?"))
    indeks=mass/(0.01*pikkus)**
    print ("! Sinu keha indeks on:", indeks)
    if indeks<16:
        vastus="Tervisele ohtlik alakaal"
    elif 16<indeks<=19:
        vastus="Alakaal"
    elif 19<indeks<=25:
        vastus="Normaalkaal"
    elif 25<indeks<=30:
        vastus="Ülekaal"
    elif 30<indeks<=35:
        vastus="Rasvumine"
    elif 35<indeks<=40:
        vastus="Tugev rasvumine"
    else indeks>40:
        vastus="Tervisele ohtlik rasvumine"
    print(vastus)

else
print("Kahju! See on väga kasulik info!")



print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

