class Student:
    def __init__(self, jmeno, vek, obor):
        self.jmeno = jmeno
        self.vek = vek
        self.obor = obor

    def predstav_se(self):
        print(f"Jsem {self.jmeno}, je mi {self.vek} let a studuji {self.obor}.")

student1 = Student("Nikola", 19, "Ekonomika")
student2 = Student ("Honza", 19, "Fyzioterapie")

print(student1.jmeno, student1.vek, student1.obor)
print(student2.jmeno, student2.vek, student2.obor)

student1.predstav_se()
student2.predstav_se()