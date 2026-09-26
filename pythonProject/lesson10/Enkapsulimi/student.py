class Studenti:
    def __init__(self, emri, mbiemri):
        self.emri=emri
        self.mbiemri=mbiemri



studenti23 = Studenti("Donjeta", "Zogaj")


studenti23.mbiemri="Hasani"
studenti23.emri="Suela"
print(studenti23.mbiemri)
print(studenti23.emri)