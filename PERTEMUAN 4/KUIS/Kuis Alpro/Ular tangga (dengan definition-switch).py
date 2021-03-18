

posisiAwal, dadu = input().split()


posisiAwal = int(posisiAwal)
dadu = int(dadu)

#Membuat fungsi switch
def switchPosisi(i):
    #membuat object atau list asosiatif sebagai dictionary
    switcher={

        3  : 21, #NAIK
        8  : 30,
        28 : 84,
        58 : 77,
        75 : 86,
        90 : 91,

        97 : 79, #TURUN
        95 : 51,
        88 : 18,
        62 : 22,
        57 : 57,
        52 : 29,
        17 : 15,

    }
    return switcher.get(i, i);


posisiAkhir = switchPosisi(posisiAwal+dadu);

if posisiAkhir >= 100 or posisiAkhir == 80:
    print("MENANG")
else:
    print(posisiAkhir)