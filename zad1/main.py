import math
a = 69.99
print("Towar kosztuje", a)

x = int(input("podaj r"))
a = (x**2) * (math.pi)
print ("Pole kola wynosi", a)

x = (('Playway', ('PLW', 310)), ('CD Project', ('CDR', 300)))
print(x[0][1][0])

day1 = ['2342', '2342', '2341', '1345']
day2 = ['23534', '23442', '234234', '234234']
day1.append(day2)
print(day1)

stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Project': 293},
    'TEN': {'Ten Squere Games':301}
}
stocks['CDR']['CD Project'] = 310
print(stocks['CDR'])