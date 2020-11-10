import random

def password_generetor():
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    simb = ['!', "%", "#", "@", "&","^","*","(",")"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = upper + lower + simb + num

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)
    
    password = "".join(password)
    return password

def run():
    password = password_generetor()
    print("Tu nueva contraseña es: " + password)

if __name__ == "__main__":
    run()