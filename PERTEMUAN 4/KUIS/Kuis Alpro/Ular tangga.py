

posisiAwal, dadu = input().split()


posisiAwal = int(posisiAwal)
dadu = int(dadu)

posisiAkhir = posisiAwal + dadu

if posisiAkhir >= 100 or posisiAkhir == 80:
    status = "MENANG"
else:
    if posisiAkhir == 3:  # Kondisi Naik
        posisiAkhir = 21
    elif posisiAkhir == 8:
        posisiAkhir = 30
    elif posisiAkhir == 28:
        posisiAkhir = 84
    elif posisiAkhir == 58:
        posisiAkhir = 77
    elif posisiAkhir == 75:
        posisiAkhir = 86
    elif posisiAkhir == 90:
        posisiAkhir = 91



    elif posisiAkhir == 97:  # Kondisi Turun
        posisiAkhir = 79
    elif posisiAkhir == 95:
        posisiAkhir = 51
    elif posisiAkhir == 88:
        posisiAkhir = 18
    elif posisiAkhir == 62:
        posisiAkhir = 22
    elif posisiAkhir == 57:
        posisiAkhir = 40
    elif posisiAkhir == 52:
        posisiAkhir = 29
    elif posisiAkhir == 17:
        posisiAkhir = 15

    status = posisiAkhir

print(status)



