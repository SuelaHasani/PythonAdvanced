class person:

    def __init__(self, emri, mosha, pesha, gjatesia):
        self.emri= emri
        self.mosha=mosha
        self._pesha=pesha
        self._gjatesia=gjatesia

    @property
    def pesha(self):
        return self._pesha

    @property
    def gjatesia(self):
        return self._gjatesia

class i_rritur(person):
    def llogarit_bmi(self):
        return self.pesha / self.gjatesia ** 2

class femij(person):
    def llogarit_bmi(self):
        return (self.pesha / self.gjatesia ** 2) * 1.3




emri = input("Emri: ")
mosha = int(input("Mosha: "))
pesha = float(input("Pesha: "))
gjatesia = float(input("Gjatesia: "))

if mosha >= 18:
    personi = i_rritur(emri, mosha, pesha, gjatesia)
else:
    personi = femij(emri, mosha, pesha, gjatesia)

print("BMI: " , personi.llogarit_bmi())