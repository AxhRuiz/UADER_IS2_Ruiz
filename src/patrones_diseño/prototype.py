#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Prototype
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------

# Cada objeto debe sacer como copiarse a si mismo

class Note(object):

    def __init__(self, fraction):
        self.fraction = fraction

    def get(self):
        return self.fraction

    def clone(self):
        return Note(self.fraction)


x=Note(10)
print("Valor almacenado en (x) fraction %d" % (x.get()))
a=x.clone()
print("Valor almacenado en (a) fraction %d" % (a.get()))



