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


jumlahBatik=0;


while a >= minKain and b >= minLilin and c >= minPewarna:
    jumlahBatik=jumlahBatik+1;
    a=a-minKain;
    b=b-minLilin;
    c=c-minPewarna;

print(jumlahBatik)


#Contoh input: 8 7 8    ||  3 2 4   ||  10 21 3