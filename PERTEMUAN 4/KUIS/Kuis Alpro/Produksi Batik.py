#Untuk membuat batik dibutuhkan:
#   2m kain, 3 lilin, dan 2 pewarna

minKain=2;
minLilin=3;
minPewarna=2;

#input stok kain, lilin, dan pewarna
a, b, c=input().split();

#merubah dari string ke integer
a=int(a)
b=int(b)
c=int(c)

#inisiasi jumlah batik di awal
jumlahBatik=0;

#pengechekan stok dan proses produksi
while a >= minKain and b >= minLilin and c >= minPewarna:
    jumlahBatik=jumlahBatik+1;
    a=a-minKain;
    b=b-minLilin;
    c=c-minPewarna;

#outputkan batik yang sudah diproduksi
print(jumlahBatik)


#Contoh input       : 8 7 8    ||  3 2 4   ||  10 21 3 ||  101 102 103  || 997 1500 1000
#Ekspektasi output  : 2        ||    0     ||     1    ||     34        ||      498