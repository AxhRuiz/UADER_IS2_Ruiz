#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Creación
#* Builder
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------

#*----- Método uno de utilizar un Builder

from typing import NamedTuple
class Port(NamedTuple):
    number: int
    name: str = ''
    protocol: str = ''

#*----- Método dos para utilizar un builder

class PortBuilder(object):
    def __init__(self, port):
        self.port = port
        self.name = None
        self.protocol = None

    def build(self):
        return Port(self.port, self.name, self.protocol)

class HTTPBuilder(object):
    def __init__(self):
       
        self.port=80
        self.name='HTTP'
        self.protocol='TCP'

    def build(self):
        return Port(self.port, self.name, self.protocol)

# The Builder lets the caller create a Port without
# needing to specify a value for every attribute.
# Here we skip providing a “name”:

a = PortBuilder(21)
a.name = 'FTP'
a.protocol='TCP'
a.build()
print(a.port,a.name,a.protocol)

b = PortBuilder(517)
b.protocol = 'UDP'
b.name = '---'
b.build()             # Aqui construye el objeto con sus atributos
print(b.port,b.name,b.protocol)

c = Port(517,'X/Y','UDP')
print(c.number,c.name,c.protocol)

z= HTTPBuilder()
z.build()
print(z.port,z.name,z.protocol)
