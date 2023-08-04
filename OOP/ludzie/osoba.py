class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.poziom_szczescia = 0

    def przedstaw_sie(self):
        return f"{self.imie} {self.nazwisko}"


class Biegacz(Osoba):

    def zrob_przebiezke(self, dystans):
        if dystans > 1:
            self.poziom_szczescia += 1


class StrongMan(Osoba):

    def podnies_ciezar(self, ciezar):
        if ciezar > 100:
            self.poziom_szczescia += 1


class BiegaczSkomplikowany(Osoba):

    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)  # odnośnik do klasy, z której dziedziczymy
        self.poprzedni_dystans = None
        self.suma_dystansow = 0

    def przedstaw_sie(self):
        print(super().przedstaw_sie())
        print("Jestem skomplikowany")

    def zrob_przebiezke(self, dystans):
        if dystans > 1:
            self.poziom_szczescia += 1  # self.poziom_szczescia = self.poziom_szczescia + 1
        self.poprzedni_dystans = dystans

        ile_pelnych_dziesiatek_poprzednio = self.suma_dystansow // 10
        self.suma_dystansow += dystans
        ile_pelnych_dziesiatek_teraz = self.suma_dystansow // 10
        ile_nowych_dziesiatek = ile_pelnych_dziesiatek_teraz - ile_pelnych_dziesiatek_poprzednio
        if ile_nowych_dziesiatek > 0:
            self.poziom_szczescia += 3*ile_nowych_dziesiatek
