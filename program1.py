print ("PROGRAM PYTHON MENGHITUNG NILAI TERKECIL & TERBESAR SERTA NILAI RATA-RATA")
n = int(input("\nMasukan Jumlah Laba = "))
bil = []
tot = 0
for x in range(n):
    m=x+1
    a = int(input("Laba ke %d = "%m))
    bil.append(a)
    tot += bil[x]
    rata2 = tot / n

print("\nLaba Bulanan: %d" %min(bil))
print("Laba Terbesar : %d" %max(bil))
print("Total laba  : %0.2f" %rata2)
