"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) Kādus ciparus jūs ziniet?
    Arābu cipari (no 0 līdz 9)
2) Kādus romiešu ciparus jūs ziniet?
    I, V, C, M, X, L, D.
3) Kas ir klase?
    Klase ir programmēšanas struktūra, kas var rediģēt datu uzvedību un metodes.
    Klase sastāv no konstruktora/destruktora un metodēm. (Iekšējām funkcijām.)
    Parametri ir klases iekšējie mainīgie.
5) Kādas datu struktūras ziniet?
    list(saraksts), arry(masīvs), dict(vārdnīca)
    a=""                          a={}, a=dict{}
    Vārdnīcu var saprast kā tabulu ar divām colonām.


"""

class AAA:
    # Jādefinē konstruktors
    def __init__(self):
        self.roma_sk={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M',
        }
    # definē nepieciešanas metodes
    def to_roman(self, num):
        result=""
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result += numeral
                num -= value #num=num-value
        return result

# piemers
skaitlis=2023
# definejam objektu
kk=AAA()
# jaunajam objektam jaizsauc klases metode
romieshu=kk.to_roman(skaitlis)


# noformēt izdruku
print(f"{skaitlis} ar romiešū cipariem ir {romieshu}.")