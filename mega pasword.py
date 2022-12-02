import random
print("F гр = G m 1 ? m 2 R 2 , где G = 6,67 ? 10 ? 11 Н ? м 2 кг 2 — гравитационная постоянная, R — расстояние между центрами тел, m 1 , m 2 — массы тел.")
var = ["1","2","3","4","5","6","7","8","9","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
while True:
    nok = int(input("Введите колличество символов: "))
    if nok >= 14:
        print("Зачем тебе такой пароль? Половина соцсетей его не поддерживают")
    elif nok <= 8:
        print("Маленькие пароли легко взламываются")
    s = ''
    for step in range(nok):  
        q = var[random.randint (0, len(var)-1)]
        s=s+q
    print(s)
    n=input("enter")
    if n=="game":
        import square
        square.main()