from ludzie.osoba import Biegacz, StrongMan, BiegaczSkomplikowany

if __name__ == '__main__':
    jas = Biegacz("Jan", "Kowal")
    stas = StrongMan("Stanisław", "Nowak")
    print(jas.przedstaw_sie())
    print(stas.przedstaw_sie())
    michal = BiegaczSkomplikowany("Michał", "Malina")
    michal.zrob_przebiezke(30)
    print(michal.przedstaw_sie())
    print(michal.poziom_szczescia)
