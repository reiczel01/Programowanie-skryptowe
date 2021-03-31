
#Zadanie 1 
#Liczby parzyste z listy [1,2,3,4,5,6,7,8] 
 
def liczby_parzyste(list): 
    licz_parzyste = [] 
 
    for numbers in list: 
        if numbers % 2 == 0: 
            licz_parzyste.append(numbers) 
        else: 
            pass 
    return licz_parzyste 
print(liczby_parzyste([1,2,3,4,5,6,7,8])) 
 
#Zadanie 2 
# Kto jest pracownikiem miesi�ca oraz ile godzin przepracowa� 
# work_hours = [('Abby',100),('Billy',400),('Cassie',800)] 
 
work_hours = [('Abby',100),('Billy',400),('Cassie',800)] 
 
def pracownik_miesi�ca(work_hours): 
    hour_max = 0 
    najlepszy_pracownik = "" 
    for pracownik, hour in work_hours: 
        if hour > hour_max: 
            hour_max = hour 
            najlepszy_pracownik = pracownik 
        else: 
            pass 
    return (hour_max, najlepszy_pracownik) 
 
print(pracownik_miesi�ca(work_hours)) 
 
#Zadanie 3 
# Funkcja, kt�ra liczy ma�e i du�e litery z zadaniu 
# Dzie� dobry, jestem z  Polski. 
 
def zdanie(s): 
    duze = 0 
    male = 0 
    for c in s: 
        if c.isupper(): 
            duze +=1 
        elif c.islower(): 
            male +=1 
        else: 
            pass 
    print(f'du�e: {duze}') 
    print(f'male: {male}') 
s = "Dzie� dobry, jestem z  Polski." 
 
zdanie(s) 
 
#Zadanie 4 
# Funkcja, kt�ra sprawdza czy string jest palindromem 
 
def palindrom(s): 
    s = s.replace(" ", "") 
    return s == s[::-1] 
s = "a kajaka" 
print(palindrom(s)) 
 
#Zadanie 5 
# Wykorzystuj�c try i except wy�wietli� napis "pojawi� si� b��d" 
# lista = ["a", "b", "c"] 
#wyswietla� ma sie kwadrat element�w w li�cie 
try: 
    for i in ["a", "b", "c"]: 
        print(i**2) 
except: 
    print("pojawi� si� b��d") 
 
#Zadanie 6 
# Napisac funkcj�, kt�ra pyta u�ytkownika o liczb� ca�kowit� i zwraca jej kwadrat. W razie gdy u�ytkownik nie poda� 
# liczby ca�kowitej ma wy�wietli� si� napis "Pojawi� si� b��d. Spr�buj jeszcze raz. Wykorzysta�: while, try, except. 
 
def ask(): 
    while True: 
        try: 
            n = int(input("podaj liczb� ca�kowit�: ")) 
            print(f"kwadrat liczby to: {n ** 2}") 
            return True 
        except: 
            continue 
 
ask() 

 

 