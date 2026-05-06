"""El patron flyweight se puede usar por ejemplo para un procesador de textos. un documento
tiene muchos caracteres, los cuales tiene una fuente tamaño y color. pero en el mismo solo usas
3 o 4 tipos de legras distintos. Con flyweight se crea un solo objeto por cada combincacion de fuente/tamaño/color
y lo compartis entre todos los caracteres que la usan."""