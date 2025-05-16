class Student:
    def __init__(self, jmeno, vek, obor):
        self.jmeno = jmeno
        self.vek = vek
        self.obor = obor

class ZahraničníStudent(Student):
    def __init__(self, jmeno, vek, obor, zeme):
        super().__init__(jmeno, vek, obor)
        self.zeme = zeme

    def __str__(self):
        return f"{self.jmeno}, {self.vek} let, obor: {self.obor}, ze země: {self.zeme}"

student3 = ZahraničníStudent("Liam", 20, "Biologie", "Kanada")
print(student3)

