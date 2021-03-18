
# input A B C dan D
a, b, c, d=input().split()

#rubah str ke float
a=float(a)
b=float(b)
c=float(c)
d=float(d)

nakBagong=float(a/b)
pakdeSemar=float(c/d)

if nakBagong > pakdeSemar:
    print(">")
elif nakBagong < pakdeSemar:
    print("<")
else:
    print("=")

# CONTOH MASUKAN 1
# 8 15 9 20
# CONTOH KELUARAN 1
# >
# CONTOH MASUKAN 2
# 4 2 100 50
# CONTOH KELUARAN 2
# =