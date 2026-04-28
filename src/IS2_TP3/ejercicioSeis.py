""""6. Dado una clase que implemente el patrón “prototipo” verifique que una clase
generada a partir de ella permite por su parte obtener también copias de si
misma."""

import copy
from abc import ABC, abstractmethod

class Prototype(ABC): #interfaz abstracta para prototype.
    
    @abstractmethod
    def clone(self): #Crea y retorna una copia exacta del objeto
        pass
class Documento(Prototype): #documento clonable que implemnta el patron
    
    def __init__(self, titulo:str, contenido: str, metdata: dict):#inicializa un nuevo document
        self.titulo = titulo
        self.contenido= contenido
        self.metdata = metdata
    
    def clone(self):
        return copy.deepcopy(self) #deepcopy garantiza copias independientes
    
    def __str__(self) -> str: #retorna una representacion legible del documento
        return(
            f"Documento:\n"
            f"  Título: {self.titulo}\n"
            f"  Contenido: {self.contenido}\n"
            f"  Metadata: {self.metdata}\n"
        )
        

def main()-> None:
    #Documento original
    Doc_org= Documento(
        titulo="Informe",
        contenido="Novedades",
        metdata= {
            "autor": "Axel R",
            "version": 1,
            "tags" : ["test, calidad"]
        }
    )
    
    print("-----Documento Original-----")
    print(Doc_org)
    
    doc_clon = Doc_org.clone()#primera copia del original
    
    doc_clon.titulo= "Informe - copia"
    doc_clon.metdata["version"]= 2
    doc_clon.metdata["tags"].append("revision")
    
    print("-----Documento Copiado Modificado-----")
    print(doc_clon)
    
    doc_clon2= doc_clon.clone()#seguda clonacion, copia de la copia
    
    doc_clon2.titulo="Informe - Copia de copia"
    doc_clon2.metdata["version"]= 3
    doc_clon2.metdata["tags"]="error"
    
    print("-----Documento - Copia de copia -----")
    print(doc_clon2)
    
if __name__ == "__main__":
    main()