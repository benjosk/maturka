def pravouhly():
    return a**2 + b**2 == c**2
def rs():
    return a==b and a==c and b==c
def rr():
    return a==b!=c or a==c!=b or b==c!=a
def rozno():
    return a != b != c
while True:
    try:
        a = float(input("zadaj stranu a v cm :"))
        b = float(input("zadaj stranu b v cm :"))
        c = float(input("zadaj stranu c v cm :"))
        if a+b < c or a+c < b or b+c < a:
            print("Trojuholník sa nedá zostrojiť")
        else:
            text = []
            if rr():
                text.append("rovnoramenný")
            elif rs():
                text.append("rovnostranný")
            elif rozno():
                text.append("rôznostranný")
            if pravouhly():
                text.append("je pravouhlý")
            else:
                text.append("nie je pravouhlý")
            print(f"Trojuholník je {text[0]} a {text[1]}.")
        break
    except ValueError:
        print("Zlá hodnota")
