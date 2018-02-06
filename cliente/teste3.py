N = float(input())
c = ciq = v = d = ci = do = u = cc = vc = dc = cic = uc = 0
N = round(N, 2)
while True:
    while N >= 100:
        N -= 100
        c += 1
    while N >= 50:
        N -= 50
        ciq += 1
    while N >= 20:
        N -= 20
        v += 1
    while N >= 10:
        N -= 10
        d += 1
    while N >= 5:
        N -= 5
        ci += 1
    while N >= 2:
        N -= 2
        do += 1
    while N >= 1:
        N -= 1
        u += 1
    N = round(N, 2)
    while N >= 0.50:
        N -= 0.50
        cc += 1
    while N >= 0.25:
        N -= 0.25
        vc += 1
    while N >= 0.10:
        N -= 0.10
        dc += 1
    while N >= 0.05:
        N -= 0.05
        cic += 1
    while N > 0.00:
        N -= 0.01
        uc += 1
    break
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(c))
print('{} nota(s) de R$ 50.00'.format(ciq))
print('{} nota(s) de R$ 20.00'.format(v))
print('{} nota(s) de R$ 10.00'.format(d))
print('{} nota(s) de R$ 5.00'.format(ci))
print('{} nota(s) de R$ 2.00'.format(do))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(u))
print('{} moeda(s) de R$ 0.50'.format(cc))
print('{} moeda(s) de R$ 0.25'.format(vc))
print('{} moeda(s) de R$ 0.10'.format(dc))
print('{} moeda(s) de R$ 0.05'.format(cic))
print('{} moeda(s) de R$ 0.01'.format(uc))
