initialcost = 305000
#folcost 6 hari
folcost = 10000
#convent 4 hari
convent = 18000
bulan = 1
#biaya 1 bulan
ecbln = initialcost + (5*folcost)
cbln = 7.5*convent
#bulan pertama
print('biaya bulan 1', ecbln, cbln)
#perhitungan kapan untung
while ecbln > cbln:
    ecbln = ecbln + 5*folcost
    cbln = cbln + 7.5*convent
    bulan = bulan + 1
    print('biaya bulan',bulan, ecbln, cbln)
print(bulan)