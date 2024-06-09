def tas_kagit_makas():

    a = input("taş kağıt makas oynamak ister misin(yes or no)").lower()

    import time
    import random
    pc_list = ["t", "k", "m"]

    while a == "yes":

        pc = pc_list[random.randint(0,2)]

        time.sleep(1)

        you = input("birini seç: t: taş, m: makas, k: kağıt").lower()

        if (pc == "t" and you == "m") or (pc == "m" and you == "k") or (pc == "k" and you == "t"):
            print("kazanan bilgisayar")
        
        elif (pc == "m" and you == "t") or (pc == "k" and you == "m") or (pc == "t" and you == "k"):
            print("kazanan sensin")

        elif (pc == "m" and you == "m") or (pc == "k" and you == "k") or (pc == "t" and you == "t"):
            print("berabere")

        else:
            print("hatalı giriş")

        time.sleep(1)

        a = input("taş kağıt makas oyununa devam etmek ister misin(yes or no)").lower()

    print("oyun bitti")