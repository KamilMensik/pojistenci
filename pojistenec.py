class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefon) -> None:
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self) -> str:
        return f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t{self.telefon}"