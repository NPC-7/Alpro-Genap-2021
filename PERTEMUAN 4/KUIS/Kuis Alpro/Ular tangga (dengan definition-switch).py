
#Inputkan Posisi Awal dan Dadu
posisiAwal, dadu = input().split()

#ubah ke Integer
posisiAwal = int(posisiAwal)
dadu = int(dadu)

#Membuat fungsi switch
def switchPosisi(posisi):
    #membuat object atau list asosiatif sebagai dictionary
    switcher={
        3  : 21, #Kondisi Naik
        8  : 30,
        28 : 84,
        58 : 77,
        75 : 86,
        80 : 100,
        90 : 91,

        97 : 79, #Kondisi Turun
        95 : 51,
        88 : 18,
        62 : 22,
        57 : 57,
        52 : 29,
        17 : 15,
    }

    # Mengambil data sesuai keyword, bila tidak ada
    # keyword yg sesuai maka balikkan nilai posisi itu sendiri
    return switcher.get(posisi, posisi);


#Definisikan posisi akhir menggunakan fungsi yg telah dibuat
posisiAkhir = switchPosisi(posisiAwal+dadu);

#check apakah posisi akhir memenuhi lebih dari sama dengan 100 atau tidak
if posisiAkhir >= 100:
    print("MENANG") #Print "MENANG" bila memenuhi
else:
    print(posisiAkhir) #Print posisiAkhir bila kurang dari 100