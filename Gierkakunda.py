from random import randint;
# ========================================WSTĘP=============================================
print("="*100)
print("Bijesz sie z Kunda,usidał na towim miejscu. ")
print("="*100)
print("")
# ========================================POSTAĆ============================================
nick = input('Podaj swój nick: ')
print("="*100)
life = 100
umiejetnosci = 1000
# ========================================CIOSY==============================================
def grzecznie_prosisz_zeby_ustapil():
    return randint(30, 50)

def wykreciles_mu_uszko():
    global umiejetnosci
    umiejetnosci -= 15
    return randint(10, 12)

def laskoczesz_go():
    global umiejetnosci
    umiejetnosci -= 25
    return randint(15, 18)

def wybierz_jak_zaatakujesz():
    print(f"{nick} wybierz atak:")
    print("P - grzecznie prosisz zeby ustapil")
    print("H - wykreciles mu uszko")
    print("O - laskoczesz go")
    jaki = input()
    if jaki.upper() == "P":
        return grzecznie_prosisz_zeby_ustapil()
    
    elif jaki.upper() == "H":
        if umiejetnosci >= 12:
            return wykreciles_mu_uszko()
        else:
            print("Nie możesz teraz tego użyć :C")
            return Kunda
    
    elif jaki.upper() == "O":
        if umiejetnosci >= 18:
            return laskoczesz_go()
        else:
            print("Nie możesz teraz tego użyć :C")
            return 0
    
    else:
        print("="*100)
        print("Zostajesz zaatakowany, następnym razem wybierz dobrze")
        print("="*100)   
        return 0
# =======================================Boss=========================================
# Kundzior = ["nazwa", ile ma hp, ile ci zabiera hp]
Kunda = ["Kunda",120, 15]

# ===================================WALKA Z KUNDZIOREM====================================

while True:
    print(f"{nick} musisz walczyć z kunda! Podejmujesz się walki?")
    print("Tak - 1, Odpuszczam jak lamus - 2")
    print("="*100)

    inp = input()
    if inp == "1":
        print("Walczysz z Kunda!")
        break
    elif inp == "2":
        print("jestes beznadziejny wroc jak zmezniejesz")
        print("="*100)
        break
    else:
        print("="*100)
        print("Wybierz dobrą opcje")
        print("="*100)

while life > 0:
    if inp == "1":
        while Kunda[1] > 0:
            print("="*100)
            print(f"Kunda ma { Kunda[1]}✽ Hp i zadaje ci {Kunda[2]}✽ Obrażeń")
            life = life - Kunda[2]
            print(f"Zostało ci {life}✽ Hp i {umiejetnosci}✽ Umiejętności")
            print("-"*40)
            atak  = wybierz_jak_zaatakujesz()
            Kunda[1] = Kunda[1] - atak
            print(f"Zadałeś {atak} obrażeń")
        print("="*100)
        print("Wygrałeś z Kunda!!!")
        if Kunda[1] <= 0:
            break
print("="*100)

